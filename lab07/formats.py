import csv
import json
import io

def csv_to_records(text: str) -> list[dict]:
    if not text.strip():
        return []

    f = io.StringIO(text.strip())
    reader = csv.DictReader(f)

    records = []
    for row in reader:
        clean_row = {}
        for key in row:
            clean_row[key.strip()] = row[key].strip()
        records.append(clean_row)

    return records

def convert_value(val: str):
    if val.lower() == 'true' or  val.lower() == 'yes':
        return True
    elif val.lower() == 'false' or  val.lower() == 'no':
        return False
    elif val.isdigit():
        return int(val)
    else:
        # if "," in val:
        #     val = val.replace(",", ".")
        return float(val)

def parse_settings(lines: list[str]) -> dict:
    result = {}
    current_key = None

    for line in lines:
        # пропускаем комментарии, т.е тоо, что после #
        line = line.split('#')[0].strip()
        if not line:
            continue

        if line.endswith(':'): # это значит в конфиге записано "имя:" и все
            current_key = line[:-1]
            result[current_key] = []
        elif line.startswith('- '):
            # Преобразование типов
            val = line[2:].strip()
            try:
                parsed_val = convert_value(val)

                if current_key:
                    result[current_key].append(parsed_val)
                else:
                    return {}
            except ValueError:
                result[current_key].append(val)
        else:
            key, val = [x.strip() for x in line.split(':', 1)]
            try:
                parsed_val = convert_value(val)

                result[key] = parsed_val
            except ValueError:
                result[key] = val
    return result

def merge_by_key(rows: list[dict], extra: dict, key: str ='id') -> list[dict]:
    for row in rows:
        if row_id in extra and key in row:
            row_id = row.get(key)
            row.update(extra[row_id])
    return rows

def records_to_json(records: list[dict]) -> str:
    # sort_keys=True для алфавитного порядка, indent=2 для отступов
    # ensure_ascii=False для сохранения кириллицы
    return json.dumps(records, indent=2, sort_keys=True, ensure_ascii=False)
