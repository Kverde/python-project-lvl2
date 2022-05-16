def format_obj(obj):
    if isinstance(obj, bool):
        return str(obj).lower()

    if isinstance(obj, dict):
        return '[complex value]'

    if obj == None:
        return 'null'

    if isinstance(obj, str):
        return f"'{str(obj)}'"

    return str(obj)


def format_plain(diff):
    lines = []

    def inner(diff, path):
        for key in diff:
            (rel, value1, value2) = diff[key]

            current_path = path + [key]
            current_path_str = '.'.join(current_path)

            if rel == 'children':
                inner(value1, current_path)
                continue

            if rel == 'same':
                continue

            if rel == 'removed':
                lines.append(f"Property '{current_path_str}' was removed")
                continue

            if rel == 'added':
                lines.append(
                    f"Property '{current_path_str}' was added with value: {format_obj(value2)}")
                continue

            lines.append(
                f"Property '{current_path_str}' was updated. From {format_obj(value1)} to {format_obj(value2)}")

    inner(diff, [])
    return '\n'.join(lines)
