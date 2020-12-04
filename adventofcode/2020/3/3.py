import os

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, 'input.txt')
file = open(file_path, 'r')

lines = file.readlines()

mp = []
for line in lines:
    row = []
    for c in line:
        if c != '\n':
            row.append(c)
    mp.append(row)

def getTrees(mp, right, down):
    i, j = 0, 0
    rows, cols = len(mp), len(mp[0])
    trees = 0

    while i < rows:
        j += right
        i += down

        if j >= cols:
            j -= cols

        if i < rows and mp[i][j] == '#':
            trees += 1
    return trees



# Right 1, down 1.
# Right 3, down 1.
# Right 5, down 1.
# Right 7, down 1.
# Right 1, down 2.

print("Trees Part 1:", getTrees(mp, 3, 1))
print("Trees Part 2:", getTrees(mp, 1, 1) * getTrees(mp, 3, 1) * getTrees(mp, 5, 1) * getTrees(mp, 7, 1) * getTrees(mp, 1, 2))
