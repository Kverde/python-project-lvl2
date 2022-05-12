
def prepare_value(obj, deep=0):

    if isinstance(obj, dict):
        offset = '    ' * deep
        res = []
        res.append('{')
        for key, value in obj.items():
            res.append(f'{offset}    {key}: {prepare_value(value, deep + 1)}')
        res.append(f'{offset}}}')
        return '\n'.join(res)

    if isinstance(obj, bool):
        return str(obj).lower()

    if obj == None:
        return 'null'

    return str(obj)


def format_stylish(diff, deep=0):
    offset = '    ' * deep

    lines = []
    lines.append('{')

    for key in diff:
        (rel, value1, value2) = diff[key]

        if rel == 'children':
            lines.append(f'{offset}    {key}: ' +
                         format_stylish(value1, deep + 1))
            continue

        if rel == 'same':
            lines.append(
                f'{offset}    {key}: {prepare_value(value1, deep + 1)}')
            continue

        if rel == 'removed':
            lines.append(
                f'{offset}  - {key}: {prepare_value(value1, deep + 1)}')
            continue

        if rel == 'added':
            lines.append(
                f'{offset}  + {key}: {prepare_value(value2, deep + 1)}')
            continue

        lines.append(f'{offset}  - {key}: {prepare_value(value1, deep + 1)}')
        lines.append(f'{offset}  + {key}: {prepare_value(value2, deep + 1)}')

    lines.append(f'{offset}}}')
    return '\n'.join(lines)


def format(diff, format_type='stylish'):
    if format_type == 'stylish':
        return format_stylish(diff)

    raise Exception(f'Usupported format type "{format_type}"')
