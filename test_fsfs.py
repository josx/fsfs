import os
import pytest
from fsfs import count_whitespace_in_file, count_whitespace_in_directory

# Sample files for testing
TEST_DIR = "test_files"
os.makedirs(TEST_DIR, exist_ok=True)

# Create sample files with known whitespace counts
sample1_path = os.path.join(TEST_DIR, "sample1.py")
with open(sample1_path, "w", encoding="utf-8") as file:
    file.write("def test():\n    pass\n")

sample2_path = os.path.join(TEST_DIR, "sample2.py")
with open(sample2_path, "w", encoding="utf-8") as file:
    file.write("        def test():\n            pass\n")

sample3_path = os.path.join(TEST_DIR, "sample3.txt")  # Non-programming file
with open(sample3_path, "w", encoding="utf-8") as file:
    file.write("        def test():\n            pass\n")


def teardown_module(module):
    # Clean up the test files and directory after all tests are done
    for root, _, files in os.walk(TEST_DIR, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
    os.rmdir(TEST_DIR)


def test_count_whitespace_in_file():
    four_space_count, eight_space_count = count_whitespace_in_file(sample1_path)
    assert four_space_count == 1
    assert eight_space_count == 0

    four_space_count, eight_space_count = count_whitespace_in_file(sample2_path)
    assert four_space_count == 0
    assert eight_space_count == 2


def test_count_whitespace_in_directory():
    file_counts, total_four_spaces, total_eight_spaces = count_whitespace_in_directory(
        TEST_DIR
    )

    # Check individual file counts
    assert file_counts["sample1.py"]["four"] == 1
    assert file_counts["sample1.py"]["eight"] == 0

    assert file_counts["sample2.py"]["four"] == 0
    assert file_counts["sample2.py"]["eight"] == 2

    # Check total counts
    assert total_four_spaces == 1
    assert total_eight_spaces == 2


def test_summary_results():
    file_counts, total_four_spaces, total_eight_spaces = count_whitespace_in_directory(
        TEST_DIR
    )

    # Check summary results
    assert sum(1 for count in file_counts.values() if count["four"] > 0) == 1
    assert sum(1 for count in file_counts.values() if count["eight"] > 0) == 1

    assert total_four_spaces == 1
    assert total_eight_spaces == 2

    # Check bytes saved calculation
    total_bytes_saved = (total_four_spaces) + (total_eight_spaces)
    assert total_bytes_saved == 3
