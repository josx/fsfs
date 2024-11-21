import os
import re
from collections import defaultdict

PROGRAMMING_EXTENSIONS = {
    ".py",
    ".java",
    ".c",
    ".cpp",
    ".h",
    ".js",
    ".ts",
    ".go",
    ".php",
    ".rb",
    ".swift",
    ".scala",
    ".html",
    ".css",
    ".scss",
    ".less",
    ".json",
    ".xml",
    ".yaml",
    ".yml",
    ".md",
    ".rst",
    ".sh",
    ".bash",
    ".bat",
    ".ps1",
    ".sql",
}


def count_whitespace_in_file(file_path):
    four_space_count = 0
    eight_space_count = 0

    with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
        for line in file:
            # Find all sequences of spaces
            space_sequences = re.findall(r" +", line)
            for sequence in space_sequences:
                if len(sequence) == 4:
                    four_space_count += 1
                elif len(sequence) >= 8:
                    eight_space_count += 1

    return four_space_count, eight_space_count


def count_whitespace_in_directory(directory):
    total_four_spaces = 0
    total_eight_spaces = 0
    file_counts = defaultdict(lambda: {"four": 0, "eight": 0})

    for root, _, files in os.walk(directory):
        for file in files:
            if any(file.endswith(ext) for ext in PROGRAMMING_EXTENSIONS):
                file_path = os.path.join(root, file)
                four_space_count, eight_space_count = count_whitespace_in_file(
                    file_path
                )
                file_counts[file]["four"] += four_space_count
                file_counts[file]["eight"] += eight_space_count
                total_four_spaces += four_space_count
                total_eight_spaces += eight_space_count

    return file_counts, total_four_spaces, total_eight_spaces


def main(directory):
    if not os.path.isdir(directory):
        print(f"'{directory}' is not a valid.")
        return

    file_counts, total_four_spaces, total_eight_spaces = count_whitespace_in_directory(
        directory
    )

    print("File counts for 4 and 8 consecutive spaces:")
    for file, counts in file_counts.items():
        if counts["four"] > 0 or counts["eight"] > 0:
            print(f"{file}: 4 spaces: {counts['four']}, 8 spaces: {counts['eight']}")

    print("\nSummary:")
    print(
        f"Total files with 4 spaces: {sum(1 for count in file_counts.values() if count['four'] > 0)}"
    )
    print(
        f"Total files with 8 spaces: {sum(1 for count in file_counts.values() if count['eight'] > 0)}"
    )
    print(f"Total occurrences of 4 spaces: {total_four_spaces}")
    print(f"Total occurrences of 8 spaces: {total_eight_spaces}")

    total_bytes_saved = (total_four_spaces) + (total_eight_spaces)
    print(
        f"You can free up {total_bytes_saved} bytes replacing tabs for spaces."
    )


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python fsfs.py <directory>")
    else:
        main(sys.argv[1])
