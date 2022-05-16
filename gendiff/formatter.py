from gendiff.formatter_stylish import format_stylish
from gendiff.formatter_plain import format_plain
from gendiff.formatter_json import format_json


def format_diff(diff, format_type='stylish'):
    if format_type == 'stylish':
        return format_stylish(diff)

    if format_type == 'plain':
        return format_plain(diff)

    if format_type == 'json':
        return format_json(diff)

    raise Exception(f'Usupported format type "{format_type}"')
