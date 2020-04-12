# Zen stuff
# import this

# Chained assignment
x = y = z = 5
assert x == y == 5

# Chained compare
assert 2 <= x <= y <= 10

# Multiple assignment
x, *y, z = 1, 2, 3, 4, 5
assert x == 1 and z == 5

# Merging dictionaries
x = {'a': 1}
y = {'b': 2}
z = {**x, **y}
print(z)

# Joining strings
x = ['a', 'b', 'c']
print('*'.join(x))