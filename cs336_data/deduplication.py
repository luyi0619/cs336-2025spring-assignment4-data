import os

from collections import defaultdict

def exact_line_deduplication(
    input_files: list[os.PathLike], output_directory: os.PathLike
):
    uniq_lines = defaultdict(int)
    for input_file in input_files:
      with open(input_file, 'r') as read_file:
        for line in read_file:
          uniq_lines[hash(line)] += 1
    
    for input_file in input_files:
      output_file = os.path.join(output_directory, os.path.basename(input_file))
      with open(input_file, 'r') as read_file, open(output_file, 'w') as write_file:
        for line in read_file:
          if uniq_lines[hash(line)] == 1:
            write_file.write(line)
