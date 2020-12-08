import os
import re

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, 'input.txt')
file = open(file_path, 'r')

lines = file.read().strip().split("\n")

def rule_parser(lines):

    bag_dict = {}

    for line in lines:
        bag, _, content = line.partition(' bags contain ')

        if bag in bag_dict:
            raise ValueError(f'double {bag}')
        if content == 'no other bags.':
            content = {}
        else:
            content = content.split(', ')
            content = [c.split(' bag')[0] for c in content]
            content = {c.split(' ', 1)[1] : int(c.split(' ', 1)[0]) for c in content}

        bag_dict[bag] = content
    return bag_dict

bags = rule_parser(lines)

def containsBag(container, bag = 'shiny gold'):
    bags = set();
    for current_bag, content in container.items():
        if bag in content:
            bags.add(current_bag)
            bags.update(containsBag(container, bag=current_bag))
    return bags

def getBags(bag = 'shiny gold'):
    if not bag:
        return 0

    counter = 0
    for bg, num in bags[bag].items():
        
        total = getBags(bg)
        counter += num + total * num
    return counter

print(getBags())