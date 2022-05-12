from gendiff.parser import parse_file


def compare(value1, value2):
    if value1 == value2:
        return 'same', value1, value2

    if isinstance(value1, dict) and isinstance(value2, dict):
        return 'children', compare_dict(value1, value2), None

    return 'update', value1, value2


def compare_dict(d1, d2):
    keys1 = set(d1)
    keys2 = set(d2)
    keys = sorted(keys1 | keys2)

    res = {}
    for key in keys:
        if key not in d1:
            res[key] = 'added', None, d2[key]
            continue

        if key not in d2:
            res[key] = 'removed', d1[key], None
            continue

        res[key] = compare(d1[key], d2[key])
    return res


def generate_diff(file1_path, file2_path):
    d1 = parse_file(file1_path)
    d2 = parse_file(file2_path)

    d1_keys = set(d1)
    d22_keys = set(d2)
    keys = sorted(d1_keys | d22_keys)
    diff = compare_dict(d1, d2)
    return diff
