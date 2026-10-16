
from stats import average_by_city, read_valid, warmest_city, max_temp
import sys

lines = sys.stdin.read().splitlines()

records = read_valid(lines)

valid_count = len(records)
print(valid_count)

print(len(lines) - valid_count)

print(max_temp(records))

# averages = average_by_city(records)
# print(averages)
