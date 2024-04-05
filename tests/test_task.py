import pytest
from code.task import *

def test_compare_both_files(tmp_path):
    # Create test files with content
    file1_content = "apple banana"
    file2_content = "banana orange"
    file1_path = tmp_path / "file1.txt"
    file2_path = tmp_path / "file2.txt"
    file1_path.write_text(file1_content)
    file2_path.write_text(file2_content)

    # Call function to compare files
    compare_both_files(str(file1_path), str(file2_path))

    # Check the content of same.txt and diff.txt
    with open(tmp_path / "same.txt", "r") as file:
        same_content = file.read().strip()
    with open(tmp_path / "diff.txt", "r") as file:
        diff_content = file.read().strip()

    # Check expected content
    expected_same_content = "I"
    expected_diff_content = "apple\norange"
    assert same_content == expected_same_content
    assert diff_content == expected_diff_content
