import os
import re

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, 'input.txt')
file = open(file_path, 'r')

lines = file.read().splitlines()

# store as (index, instruction, value)
program = []
for index, line in enumerate(lines):
    [operation, argument] = line.split(' ')
    sign, digit = argument[0], argument[1:]

    program.append([operation, int(digit) if sign == '+' else -1 * int(digit)])

def findLoop(prog, cur, visited, accumulator):
    if cur in visited:
        return -1

    visited.add(cur)
    (operation, digit) = prog[cur]


    if operation == 'acc':
        accumulator += digit
        return findLoop(prog, cur + 1, visited, accumulator)
    elif operation == 'jmp':
        cpy = program.copy()
        cpy[cur][1] = 'nop'

        res = findLoop(prog, cur + digit, visited, accumulator)
        res2 = findLoop(cpy, 0, visited, accumulator)

        if res == -1:
            return res2
    elif operation == 'nop':
        cpy = program.copy()
        cpy[cur][1] = 'jmp'
        res = findLoop(prog, cur + 1, visited, accumulator)
        res2 = findLoop(cpy, cur + 1, visited, accumulator)

        if res == -1:
            return res2

    return accumulator

print(findLoop(program, 0, set(), 0))
