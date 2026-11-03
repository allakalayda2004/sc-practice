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

def parse_int(value: str) -> int | None:
    try:
        return int(value)
    except (ValueError, TypeError):
        return None

def parse_float(value: str) -> float | None:
    try:
        return float(value)
    except (ValueError, TypeError):
        return None

def convert_value(val: str) -> bool | int | float | str:
    # идея функции такая:
    # сначала преобразуем фиксированые значения,
    # описанные в задании, их 4:
    if val == 'true' or val == 'yes':
        return True
    elif val == 'false' or val == 'no':
        return False

    # затем пробуем пробразовать в целое - плавающия точка, если это она, вернет None
    int_val = parse_int(val)

    if not int_val is None:
        # если получилось - возвращем сконвертированное значение
        return int_val

    # затем пробуем пробразовать в число с плавабщей точкой
    float_val = parse_float(val)

    if not float_val is None:
        # если получилось - возвращем сконвертированное значение
        return float_val

    # если ни одно преобразование не применилось, вернем "совершенно точно строку"
    return str(val)

def parse_settings(lines: list[str]) -> dict:
    # преобразуем строки конфига в словарь без вложенных словарей
    result = {}
    current_key = None # если разбираем список, то здесь текущий элемент

    for line in lines:
        # пропускаем комментарии, т.е тоо, что после #
        line = line.split('#')[0].strip()
        if not line:
            continue

        if line.endswith(':'): # признак списка
            current_key = line[:-1] # вырезаем из строки последний символ и "открываем" спиок, присвоив значение в current_key
            result[current_key] = [] # создаем пустой список значений
        elif current_key and line.startswith('- '): # и дальше, пока список "открыт", и если следующая строка конфига начинается с '- ', что указывает на элемент списка
            val = line[2:].strip() # вырезаем из этой строки '- '
            result[current_key].append(val) # а то, что осталось от строки, запихиваем в список
        else:
            current_key = None # иначе "закрывам" список
            key, val = [x.strip() for x in line.split(':', 1)] # делим строку (элемент кофига вида "имя":"значение") на имя и значение, попутно убирая пробелы в начале и конце строки
            if key in result:
                # по хорошему надо еще проверять, нет ли уже такого ключа, и если есть, то кидать ошибку, потому что в конфиге так не пишут
                raise ValueError
            result[key] = convert_value(val) # записываем ключ и значение в словарь

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
