import os

def count_by_extension(paths: list[str]) -> dict[str, int]:
    result = {}
    for path in paths:
        filename = os.path.basename(path)
        if filename.find('.', 1) > 0:
            ext = filename.split('.')[-1].lower()
        else:
            ext = ""
        result[ext] = result.get(ext, 0) + 1
    return result

def deepest_path(paths: list[str]) -> str:
    if not paths:
        return ""

    deepest = ""
    max_depth = -1

    for path in sorted(paths):
        depth = path.count("/")
        if depth > max_depth:
            deepest = path
            max_depth = depth

    return deepest

def human_size(n_bytes: int) -> str:
    if n_bytes == 0:
        return "0 B"

    units = ['Б', 'КБ', 'МБ', 'ГБ', 'ТБ']
    i = 0
    size = float(n_bytes)

    while size >= 1024 and i < len(units) - 1:
        size /= 1024
        i += 1

    if size == int(size):
        return f"{int(size)} {units[i]}"
    else:
        return f"{size:.1f} {units[i]}"
