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
    if val.lower() == 'true':
        val = True
    elif val.lower() == 'false':
        val = False
    elif val.isdigit():
        val = int(val)
    else:
        val = float(val)
    return val

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
            try:
                val = convert_value(line[2:].strip())

                if current_key:
                    result[current_key].append(val)
                else:
                    return {}
            except ValueError:
                pass
        else:
            key, val = [x.strip() for x in line.split(':', 1)]
            try:
                val = convert_value(line[2:].strip())

                result[key] = val
            except ValueError:
                pass
    return result

def merge_by_key(rows: list[dict], extra: dict, key: str ='id') -> list[dict]:
    for row in rows:
        row_id = row.get(key)
        if row_id in extra:
            row.update(extra[row_id])
    return rows

def records_to_json(records: list[dict]) -> str:
    # sort_keys=True для алфавитного порядка, indent=2 для отступов
    # ensure_ascii=False для сохранения кириллицы
    return json.dumps(records, indent=2, sort_keys=True, ensure_ascii=False)
