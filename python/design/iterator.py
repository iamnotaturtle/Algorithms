# Uses an object to traverse a sequence
# Decouples algorithm from sequence

# Iterator
seq = [1, 'abc', 'a']
it = iter(seq)

try:
  while True:
     print(next(it))
except StopIteration:
  pass

# Generator
def fib(n):
  if n == 0 or n == 1:
    yield(1)

  a = 1
  b = 1
  for i in range(n):
    yield(b)
    [a, b] = [b, a + b]

it = fib(5)
try:
  while True:
     print(next(it))
except StopIteration:
  pass