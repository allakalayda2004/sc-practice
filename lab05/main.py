import logstats
import sys


top_n_errors = 3 if len(sys.argv) < 2 else int(sys.argv[1])
filename = input().strip() if len(sys.argv) < 3  else sys.argv[2]


with open(filename, 'r', encoding='utf-8') as f:
    counts = logstats.count_levels(f)


with open(filename, 'r', encoding='utf-8') as f:
    errors = logstats.top_errors(f, top_n_errors)


total = sum(counts.values())
print(total)
print(counts.get("ERROR", 0))
print(counts.get("BROKEN", 0))


report = logstats.format_report(counts, errors)
with open('report.txt', 'w', encoding='utf-8') as f:
    f.write(report)

