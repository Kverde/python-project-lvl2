import pytest

from gendiff.diff import generate_diff


FILE1_JSON_PATH = './tests/fixtures/file1.json'
FILE2_JSON_PATH = './tests/fixtures/file2.json'

FILE1_YAML_PATH = './tests/fixtures/file1.yml'
FILE2_YAML_PATH = './tests/fixtures/file2.yml'

RESULT_PATH = './tests/fixtures/result.txt'


@pytest.fixture
def correct_result():
    with open(RESULT_PATH) as f:
        return f.read()


def test_generate_diff_json(correct_result):
    actual_result = generate_diff(FILE1_JSON_PATH, FILE2_JSON_PATH)

    assert actual_result == correct_result


def test_generate_diff_yaml(correct_result):
    actual_result = generate_diff(FILE1_YAML_PATH, FILE2_YAML_PATH)

    assert actual_result == correct_result
