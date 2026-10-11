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
    
    return {"city":city, "temperature": t, "date": date} 


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
    city_counter = {}

    for line in lines:
        c = line["city"]
        t = line["temperature"]
        
        res[c] = res.get(c, 0) + t
        city_counter[c] = city_counter.get(c, 0) + 1

    avg_res = {}

    for c in res:
        avg_res[c] = round(res[c] / city_counter[c], 1)

    return avg_res


    return res    

def warmest_city(lines):
    dict = {}
    city_counter = {}

    for record in lines:
        city = record["city"]
        temp = record["temperature"]
		
        dict[city] = dict.get(city, 0) + temp
        city_counter[city] = city_counter.get(city,0) + 1
		
    sorted_cities = sorted(dict) 

    max_avg_city = ""
    max_temp = -99
    avg = 0

    for city in sorted_cities:
        avg = dict[city] / city_counter[city]

    if avg > max_temp:
        max_temp = avg
        max_avg_city = city

    return max_avg_city 

    

#parse_record("azov;15;12.12.2026") 
#parse_record("azov;15") 