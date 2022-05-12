import pytest

from gendiff.diff import generate_diff


FILE1_JSON_PLAIN_PATH = './tests/fixtures/plain/file1.json'
FILE2_JSON_PLAIN_PATH = './tests/fixtures/plain/file2.json'

FILE1_YAML_PLAIN_PATH = './tests/fixtures/plain/file1.yml'
FILE2_YAML_PLAIN_PATH = './tests/fixtures/plain/file2.yml'

RESULT_PLAIN_PATH = './tests/fixtures/plain/result.txt'


FILE1_JSON_TREE_PATH = './tests/fixtures/tree/file1.json'
FILE2_JSON_TREE_PATH = './tests/fixtures/tree/file2.json'

FILE1_YAML_TREE_PATH = './tests/fixtures/tree/file1.yml'
FILE2_YAML_TREE_PATH = './tests/fixtures/tree/file2.yml'

RESULT_TREE_PATH = './tests/fixtures/tree/result.txt'


@pytest.fixture
def correct_pain_result():
    with open(RESULT_PLAIN_PATH) as f:
        return f.read()


def test_generate_diff_plain_json(correct_pain_result):
    actual_result = generate_diff(FILE1_JSON_PLAIN_PATH, FILE2_JSON_PLAIN_PATH)

    assert actual_result == correct_pain_result


def test_generate_diff_plain_yaml(correct_pain_result):
    actual_result = generate_diff(FILE1_YAML_PLAIN_PATH, FILE2_YAML_PLAIN_PATH)

    assert actual_result == correct_pain_result


@pytest.fixture
def correct_tree_result():
    with open(RESULT_TREE_PATH) as f:
        return f.read()


def test_generate_diff_tree_json(correct_tree_result):
    actual_result = generate_diff(FILE1_JSON_TREE_PATH, FILE2_JSON_TREE_PATH)

    assert actual_result == correct_tree_result


def test_generate_diff_tree_yaml(correct_tree_result):
    actual_result = generate_diff(FILE1_YAML_TREE_PATH, FILE2_YAML_TREE_PATH)

    assert actual_result == correct_tree_result
