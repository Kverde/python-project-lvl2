
import json
import yaml

FILE_TYPE_JSON = 1
FILE_TYPE_YAML = 2


def get_file_type(filename):
    if filename.endswith('.json'):
        return FILE_TYPE_JSON

    if filename.endswith('.yml') or filename.endswith('.yaml'):
        return FILE_TYPE_YAML

    raise Exception(f'Usuppoerted file type "{filename}"')


def parse_file(filename):
    file_type = get_file_type(filename)

    if file_type == FILE_TYPE_JSON:
        return json.load(open(filename))

    if file_type == FILE_TYPE_YAML:
        return yaml.load(open(filename), yaml.SafeLoader)
