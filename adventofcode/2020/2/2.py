import os
from collections import Counter

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, 'input.txt')
file = open(file_path, 'r')

lines = file.readlines()

valid = 0
for line in lines:
    [rng, letter, password] = line.split(' ')
    [low, hi] = rng.split('-')
    rnge = set([*range(int(low), int(hi) + 1)])
    
    letter = letter[0]
    
    pword = Counter(password)
    if letter in pword and pword[letter] in rnge:
        valid += 1
print("Valid, part 1:", valid)

valid = 0
for line in lines:
    [rng, letter, password] = line.split(' ')
    [low, hi] = rng.split('-')
    low, hi = int(low), int(hi)
    
    letter = letter[0]
    
    if (password[low - 1] == letter and password[hi - 1] != letter) or (password[low - 1] != letter and password[hi - 1] == letter):
        valid += 1
print("Valid, part 2:", valid)