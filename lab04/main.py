
from stats import average_by_city, read_valid, warmest_city
import sys

#lines = sys.stdin.read().splitlines()
lines = []
err_lines = 0

while True:
    try:
        line = input()

        if line == "":
            err_lines = err_lines + 1
            break

        lines.append(line)
    except EOFError:
        err_lines = err_lines + 1
        break

records = read_valid(lines)

valid_count = len(records)
print(valid_count)

print(err_lines)

city = warmest_city(records)
print(city)


# averages = average_by_city(records)
# print(averages)
