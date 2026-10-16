from collections import Counter


def is_valid_level(level: str) -> bool:
    return level == 'DEBUG' or level == 'INFO' or level == 'WARNING' or level == 'ERROR'


def parse_event(line: str) -> dict:
    """Разбирает строку журнала на словарь."""
    parts = line.strip().split(' ', maxsplit=2)
    if len(parts) < 3 or not is_valid_level(parts[1]):
        raise ValueError("Негодная строка")
    return {"time": parts[0], "level": parts[1], "message": parts[2]}


def count_levels(lines) -> dict:
    counts = Counter()
    for line in lines:
        try:
            event = parse_event(line)
            counts[event["level"]] += 1
        except ValueError:
            counts["BROKEN"] += 1
    return dict(counts)



