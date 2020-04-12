def add(x):
  return lambda y: x + y

def mult(x):
  return lambda y: x * y

assert add(5)(5) == 10
assert mult(5)(5) == 25