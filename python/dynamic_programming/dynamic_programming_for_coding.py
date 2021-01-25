# Problems from Dynamic Programming for Coding Interviews
from typing import List

def recursiveSum(n:int) -> int:
    if n == 0 or n == 1:
        return n
    return n + recursiveSum(n - 1)

print(recursiveSum(5))

def recursiveFactorial(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    return n * recursiveFactorial(n - 1)

def factorial(n: int) -> int:
    factorial = 1

    for i in range(2, n + 1):
        factorial *= i
    return factorial

print(recursiveFactorial(5), factorial(5))

# Question 1.2
def recursiveArraySum(nums: List[int]) -> List[int]:
    if len(nums) < 2:
        return nums
    nums[1] = nums[0] + nums[1]
    return [nums[0]] + recursiveArraySum(nums[1:])

print(recursiveArraySum([1,2,3,4,5,6]))

# Example 1.2
def power(x: int, n: int) -> int:
    if n == 0:
        return 1
    elif x == 1:
        return x
    return x * power(x, n - 1)

print(power(2, 4))

# Example 1.3, Tower of Hanoi
def towerOfHanoi(source, destination, extra, n):
  if n <= 0:
    return
  towerOfHanoi(source, extra, destination, n - 1)
  print(f'Move disk {n} from {source} to {destination}')
  towerOfHanoi(extra, destination, source, n - 1)

towerOfHanoi("s", "d", "e", 3)

# 1.7
# Head recursion
def traverse(node):
    if not node:
        return
    traverse(node.next)
    print(node.val)

# Tail recursion, can also be rewritten as loop
def traverseTail(node):
    if not node:
        return
    print(node.val)
    traverseTail(node.next)

# 1.8, cannot use head or tail recursion
def inorder(node):
    if not node:
        return

    # Checking for existence before calling reduces the number of calls!
    if node.left:
        inorder(node.left)
    print(node.val)
    if node.right:
        inorder(node.right)