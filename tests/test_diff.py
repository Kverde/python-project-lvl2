from gendiff.diff import generate_diff


FILE1_PATH = './tests/fixtures/file1.json'
FILE2_PATH = './tests/fixtures/file2.json'
RESULT_PATH = './tests/fixtures/result.txt'


def test_generate_diff():
    with open(RESULT_PATH) as f:
        correct_result = f.read()

    actual_result = generate_diff(FILE1_PATH, FILE2_PATH)

    assert actual_result == correct_result
