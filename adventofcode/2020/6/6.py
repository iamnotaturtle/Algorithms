import os
import re

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, 'input.txt')
file = open(file_path, 'r')

data = file.read()
groups = data.split('\n\n')

count = 0

for group in groups:
    answers = re.split('\n', group)

    unique = {}
    total = len(answers)

    for answer in answers:
        for c in answer:
            unique[c] = unique[c] + 1 if c in unique else 1

    for key in unique:
        if unique[key] == total:
            count += 1 
