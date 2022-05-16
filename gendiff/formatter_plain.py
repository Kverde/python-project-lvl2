def format_obj(obj):
    if isinstance(obj, bool):
        return str(obj).lower()

    if isinstance(obj, dict):
        return '[complex value]'

    if obj is None:
        return 'null'

    if isinstance(obj, str):
        return f"'{str(obj)}'"

    return str(obj)


MSG_REMOVE = "Property '{prop_name}' was removed"
MSG_ADDED = "Property '{prop_name}' was added with value: {added_value}"
MSG_UPDATE = "Property '{prop_name}' was updated. From {value1} to {value2}"


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
                lines.append(MSG_REMOVE.format(prop_name=current_path_str))
                continue

            if rel == 'added':
                lines.append(MSG_ADDED.format(
                    prop_name=current_path_str,
                    added_value=format_obj(value2)
                ))
                continue

            lines.append(MSG_UPDATE.format(
                prop_name=current_path_str,
                value1=format_obj(value1),
                value2=format_obj(value2)
            ))

    inner(diff, [])
    return '\n'.join(lines)
