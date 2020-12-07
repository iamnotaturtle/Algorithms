import os
import re 

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, 'input.txt')
file = open(file_path, 'r')

data = file.read()
groups = data.split('\n\n')

passport = set([
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid'
])
´
eyecolor = set([
    'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'
])

valid = 0
for group in groups[:-1]:
    fields = re.split('\n| ', group)

    count = 0
    for field in fields:
        [key, value] = field.split(':')
        
        if key == 'byr' and 1920 <= int(value) <= 2002:
            count += 1
        elif key == 'iyr' and 2010 <= int(value) <= 2020:
            count += 1
        elif key == 'eyr' and 2020 <= int(value) <= 2030:
            count += 1
        elif key == 'hgt' and ((value[-2:] == 'cm' and 150 <= int(value[:-2]) <= 193) or (value[-2:] == 'in' and 59 <= int(value[:-2]) <= 76)):
            count += 1
        elif key == 'hcl' and re.match("^#[0-9a-f]{6}$", value):
            count += 1
        elif key == 'ecl' and value in eyecolor:
            count += 1
        elif key == 'pid' and re.match('^[0-9]{9}$', value):
            count += 1

    print ("count:", count, fields)
    if count == len(passport):
        valid += 1

print("Valid passports:", valid)


# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
#     If cm, the number must be at least 150 and at most 193.
#     If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.
