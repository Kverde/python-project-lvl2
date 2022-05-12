import json


def read_file(filename):
    with open(filename) as f:
        return f.read()


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
    json1 = json.loads(read_file(file1_path))
    json2 = json.loads(read_file(file2_path))

    json1_keys = set(json1)
    json2_keys = set(json2)
    keys = sorted(json1_keys | json2_keys)
    difference = compare_dict(json1, json2)

    lines = []
    lines.append('{')

    for key in keys:
        rel = difference[key]

        if rel == 'same':
            lines.append(f'    {key}: {prepare_value(json1[key])}')
            continue

        if rel == 'removed':
            lines.append(f'  - {key}: {prepare_value(json1[key])}')
            continue

        if rel == 'added':
            lines.append(f'  + {key}: {prepare_value(json2[key])}')
            continue

        lines.append(f'  - {key}: {prepare_value(json1[key])}')
        lines.append(f'  + {key}: {prepare_value(json2[key])}')

    lines.append('}')
    return '\n'.join(lines)
