from collections import Counter

def is_valid_level(level: str) -> bool:
    return level == 'DEBUG' or level == 'INFO' or level == 'WARNING' or level == 'ERROR'

def count_levels(lines) -> dict:
    counts = Counter()
    for line in lines:
        try:
            event = parse_event(line)
            counts[event["level"]] += 1
        except ValueError:
            counts["BROKEN"] += 1
    return dict(counts)
