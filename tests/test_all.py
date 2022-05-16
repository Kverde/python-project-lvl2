import pytest

from gendiff.diff_generator import generate_diff


FILE1_JSON_PLAIN_PATH = './tests/fixtures/plain/file1.json'
FILE2_JSON_PLAIN_PATH = './tests/fixtures/plain/file2.json'

FILE1_YAML_PLAIN_PATH = './tests/fixtures/plain/file1.yml'
FILE2_YAML_PLAIN_PATH = './tests/fixtures/plain/file2.yml'

RESULT_PLAIN_STYLISH_PATH = './tests/fixtures/plain/result_stylish.txt'


FILE1_JSON_TREE_PATH = './tests/fixtures/tree/file1.json'
FILE2_JSON_TREE_PATH = './tests/fixtures/tree/file2.json'

FILE1_YAML_TREE_PATH = './tests/fixtures/tree/file1.yml'
FILE2_YAML_TREE_PATH = './tests/fixtures/tree/file2.yml'

RESULT_TREE_STYLISH_PATH = './tests/fixtures/tree/result_stylish.txt'
RESULT_TREE_PLAIN_PATH = './tests/fixtures/tree/result_plain.txt'


@pytest.fixture
def correct_pain_stylish():
    with open(RESULT_PLAIN_STYLISH_PATH) as f:
        return f.read()


def test_generate_diff_plain_json(correct_pain_stylish):
    actual_result = generate_diff(FILE1_JSON_PLAIN_PATH, FILE2_JSON_PLAIN_PATH)

    assert actual_result == correct_pain_stylish


def test_generate_diff_plain_yaml(correct_pain_stylish):
    actual_result = generate_diff(FILE1_YAML_PLAIN_PATH, FILE2_YAML_PLAIN_PATH)

    assert actual_result == correct_pain_stylish


@pytest.fixture
def correct_tree_stylish():
    with open(RESULT_TREE_STYLISH_PATH) as f:
        return f.read()


@pytest.fixture
def correct_tree_plain():
    with open(RESULT_TREE_PLAIN_PATH) as f:
        return f.read()


def test_generate_diff_tree_json(correct_tree_stylish, correct_tree_plain):
    actual_result_stylish = generate_diff(
        FILE1_JSON_TREE_PATH, FILE2_JSON_TREE_PATH, 'stylish')
    assert actual_result_stylish == correct_tree_stylish

    actual_result_plain = generate_diff(
        FILE1_JSON_TREE_PATH, FILE2_JSON_TREE_PATH, 'plain')
    assert actual_result_plain == correct_tree_plain


def test_generate_diff_tree_yaml(correct_tree_stylish, correct_tree_plain):
    actual_result_stylish = generate_diff(
        FILE1_YAML_TREE_PATH, FILE2_YAML_TREE_PATH, 'stylish')
    assert actual_result_stylish == correct_tree_stylish

    actual_result_plain = generate_diff(
        FILE1_YAML_TREE_PATH, FILE2_YAML_TREE_PATH, 'plain')
    assert actual_result_plain == correct_tree_plain
