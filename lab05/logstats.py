from collections import Counter

def is_valid_level(level: str) -> bool:
    return level == 'DEBUG' or level == 'INFO' or level == 'WARNING' or level == 'ERROR'
