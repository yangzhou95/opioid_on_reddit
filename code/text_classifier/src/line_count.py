import glob, os
import logging


ignoreFiles = []


def get_files_in_directory(current_dir):
    os.chdir(current_dir)

    return glob.glob("*.csv")


def count_lines_one_file(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


directory = 'data/need/half-day-need'
total_count_lines = 0

files = get_files_in_directory(current_dir=directory)
for f in files:
    if f in ignoreFiles:
        continue
    line_count = count_lines_one_file(f)
    total_count_lines = total_count_lines + line_count

print("Total count lines:", total_count_lines)
