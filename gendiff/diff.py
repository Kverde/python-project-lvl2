from gendiff.parser import parse_file


def compare_dict_value(d1, d2, key):
    if key in d1 and key in d2:
        if d1[key] == d2[key]:
            return 'same'
        else:
            return 'update'

    if key in d1:
        return 'removed'

    return 'added'


def compare_dict(d1, d2):
    keys1 = set(d1)
    keys2 = set(d2)
    keys = sorted(keys1 | keys2)

    res = {}
    for key in keys:
        res[key] = compare_dict_value(d1, d2, key)
    return res


def prepare_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    return str(value)


def generate_diff(file1_path, file2_path):
    d1 = parse_file(file1_path)
    d2 = parse_file(file2_path)

    d1_keys = set(d1)
    d22_keys = set(d2)
    keys = sorted(d1_keys | d22_keys)
    difference = compare_dict(d1, d2)

    lines = []
    lines.append('{')

    for key in keys:
        rel = difference[key]

        if rel == 'same':
            lines.append(f'    {key}: {prepare_value(d1[key])}')
            continue

        if rel == 'removed':
            lines.append(f'  - {key}: {prepare_value(d1[key])}')
            continue

        if rel == 'added':
            lines.append(f'  + {key}: {prepare_value(d2[key])}')
            continue

        lines.append(f'  - {key}: {prepare_value(d1[key])}')
        lines.append(f'  + {key}: {prepare_value(d2[key])}')

    lines.append('}')
    return '\n'.join(lines)
