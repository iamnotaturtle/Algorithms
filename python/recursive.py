
# 1
def recursiveFactorial(n):
  if n <= 1:
    return n
  return n * recursiveFactorial(n - 1)

print(recursiveFactorial(4))

def iterativeFactorial(n):
  if n <= 1:
    return n

  factorial = 1
  for i in range(1, n + 1):
    factorial *= i
  return factorial


print(iterativeFactorial(4))

# 2
def recursiveArraySum(a, pos):
  if pos == 0:
    return a[0]
  a[pos] += recursiveArraySum(a, pos - 1)
  return a[pos]

a = [1, 2, 3, 4, 5, 6]
recursiveArraySum(a, len(a) - 1)
print(a)

# 3
def recursivePower(x, n):
  if n == 0:
    return 1
  if x == 1:
    return x
  return x * recursivePower(x, n - 1)

print(recursivePower(2, 3))

# 4
def towerOfHanoi(source, destination, extra, n):
  if n <= 0:
    return
  towerOfHanoi(source, extra, destination, n - 1)
  print(f'Move disk {n} from {source} to {destination}')
  towerOfHanoi(extra, destination, source, n - 1)

towerOfHanoi("s", "d", "e", 3)