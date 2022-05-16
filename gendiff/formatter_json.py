import json


def format_json(diff):
    def inner(diff):
        result = {}

        for key in diff:
            (rel, value1, value2) = diff[key]

            if rel == 'children':
                result[key] = inner(value1)
                continue

            if rel == 'same':
                result[key] = value1
                continue

            if rel == 'removed':
                result['-' + key] = value1
                continue

            if rel == 'added':
                result['+' + key] = value2
                continue

            result['-' + key] = value1
            result['+' + key] = value2

        return result

    result = inner(diff)
    return json.dumps(result, indent=4)
