import os

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, 'input.txt')
file = open(file_path, 'r')

lines = file.readlines()

rows = [i for i in range(128)]
cols = [i for i in range(8)]

def binarySearch(directions, rng):

    lo, hi = 0, len(rng) - 1
    isFB = directions[0] == 'B' or directions[0] == 'F'

    for direction in directions:
        mid = (lo + hi) // 2

        if direction == 'B' or direction == 'R':
            lo = mid + 1
        elif direction == 'F' or direction == 'L':
            hi = mid

    return rng[hi] if isFB else rng[lo]

# Hardcoded but can be gotten from input
maxRow = 117
maxCol = 7

seats = [[0 for i in range(maxCol + 1)] for i in range(maxRow + 1)]

for line in lines:
    [r, c] = line[:8], line[7:]

    row = binarySearch(r, rows)
    col = binarySearch(c, cols)

    if row * 8 + col == 697 or row * 8 + col == 695:
        print('HEY', line, row, col)

    seats[row][col] = 1

# print(seats)
for r in range(9, maxRow - 1):
    for c in range(maxCol):
        if (seats[r][c] == 0):
            print("nice", r, c, seats[r][c])

print(87 * 8)