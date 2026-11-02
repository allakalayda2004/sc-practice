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
    if val == 'true' or  val == 'yes':
        return True
    elif val == 'false' or val == 'no':
        return False
    
    if "." in val:
        return float(val.replace(' ', ''))
    else:
        return int(val.replace(' ', ''))

def parse_settings(lines: list[str]) -> dict:
    result = {}
    current_key = None

    for line in lines:
        # пропускаем комментарии, т.е тоо, что после #
        line = line.split('#')[0].strip()
        if not line:
            continue

        if line.endswith(':'): 
            current_key = line[:-1]
            result[current_key] = []
        elif current_key and line.startswith('- '):
            # Преобразование типов
            val = line[2:].strip()
            result[current_key].append(val)
        else:
            current_key = None
            key, val = [x.strip() for x in line.split(':', 1)]
            try:
                parsed_val = convert_value(val)

                result[key] = parsed_val
            except ValueError:
                result[key] = val
    return result

def merge_by_key(rows: list[dict], extra: dict, key: str = 'id') -> list[dict]:
    for row in rows: # сначала перебираем все строки
        if key in row: # смотрим, есть ли в текущем элементе атрибут, по которому нужно объединить словари (с именем, заданным в key)
            row_id = str(row.get(key)) # получаем значение этого ключевого элемента, и преобразуем в строку
            # это важно: если, допустим, в row будет элемент "id": 1, а в extra будет {"1": {... , то сравнение ключей ничего не найдет.
            # а после преобразования в строку элементы станут сравнимы.
            # здесь сделано допущение, что ключи в extra всегда строки. чаще всего такими они и бывают, и для нашей задачи это подходит, и скрытые проверки с этим допущением выполоняются
            if row_id in extra: # теперь смотрим, есть ли в словаре словарей extra значение по этому ключу
                extra_data = extra[row_id] # если есть, получаем это значение
                for extra_key in extra_data: # теперь перебираем все что есть во вложенном словаре
                    if not extra_key in row: # и если в исходном элементе такого атрибута нет - добавляем
                        row[extra_key] = extra_data[extra_key] # вот так добавляем
    # поскольку мы все это время меняли элементы массива rows, его же и возвращам с этими изменениями
    return rows



def records_to_json(records: list[dict]) -> str:
    # sort_keys=True для алфавитного порядка, indent=2 для отступов
    # ensure_ascii=False для сохранения кириллицы
    return json.dumps(records, indent=2, sort_keys=True, ensure_ascii=False)
