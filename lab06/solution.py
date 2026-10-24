import os

def count_by_extension(paths: list[str]) -> dict[str, int]:
    result = {}
    for path in paths:
        filename = os.path.basename(path)
        if '.' in filename:
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

