def parse_record (line):
    parts = line.split(";")
    print(parts)

    if len(parts) != 3:
        raise ValueError("Должно быть три поля")
    
    city = parts[0]
    temp = parts[1]
    date = parts[2]

    try:
        t = float(temp)
    except ValueError: 
        raise ValueError("Ошибка с температурой") 
    if city == "":
        raise ValueError("Город пустой")

    if date == "":
        raise ValueError("Дата пустая")
    
    return {"city":city, "temp": temp, "date": date} 


def read_valid(lines):
    res = []

    for line in lines:
        if line.strip() != "": 
            try:
                l = parse_record(line)
                res.append(l)
            except ValueError: 
                continue 
    return res          


def average_by_city(lines):
    res = {}

    for line in lines:
        c = line["city"]
        t = line["temp"]
        
        res[c] = res.get(c, 0) + temp
        city_counter[c] = city_counter.get(c, 0) + 1

    avg_res = {}

    for c in res:
        avg_res[c] = round(res[c] / city_counter[c], 1)

    return avg_res


    return res    


    
    

parse_record("azov;15;12.12.2026")
parse_record("azov;15") 