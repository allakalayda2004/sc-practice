
from stats import average_by_city, read_valid, warmest_city
import sys
print('Hello')

#lines = sys.stdin.read().splitlines()
lines = []

while True:
    try:
        line = input()

        if line == "":
            break

        lines.append(line)
    except EOFError:
        break

records = read_valid(lines)

valid_count = len(records)
print(valid_count)

city = warmest_city(records)
print(city)


averages = average_by_city(records)
print(averages)
