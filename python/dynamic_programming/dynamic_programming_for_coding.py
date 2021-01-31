# Problems from Dynamic Programming for Coding Interviews
# Two conditions of DP:
# Optimal substructure (problem can be solved from optimal solution to subproblems)
# Overlapping subproblems: same problem solved more than once
# Bottom up: solve from smallest amount up
# Top down: opposite
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

# 1.11
# Recursion: 
# Sort n elements
# Just move the largest element to the end
# Sort n - 1 elements
def recursiveBubbleSort(arr, n):
    if n <= 1:
        return
        
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    recursiveBubbleSort(arr, n - 1)
    return arr

print("Recursive bubble sort:", recursiveBubbleSort([7, 4, 3, 1, 8], 5))
assert(recursiveBubbleSort([7, 4, 3, 1, 8], 5) == [1, 3, 4, 7, 8])

# 1.12 mathematical table
def printMathematicalTable(n, i = 1):
    if i > 12:
        return
    print(f"{n} * {i} = {n * i}")
    printMathematicalTable(n, i + 1)

printMathematicalTable(7)

# 4.2
def nonRecursiveFib(n):
    a, b = 0, 1

    for i in range(n):
        a, b = b, a + b
    
    return a

print(nonRecursiveFib(20))

# 4.2 Example
cost = [[]]
def calculcateMinCost(s: int, d: int) -> int:
    if s == d or s == d - 1:
        return cost[s][d]
    
    minCost = cost[s][d]
    for i in range(s + 1, d):
        minCost = min(
            minCost, 
            calculateMinCost(s, i) + calculcateMinCost(i, d)
        )
    return minCost

# Memoization is recursion + cache - overlapping subproblems
memo = [[]]
def calculateMinCostMemoized(s, d):
    if s == d or s == d - 1:
        return cost[s][d]
    
    if memo[s][d] == 0:
        minCost = cost[s][d]
        for i in range(s + 1, d):
            minCost = min(
                minCost, 
                calculateMinCost(s, i) + calculcateMinCost(i, d)
            )
        memo[s][d] = minCost

    return memo[s][d] 

minCost = []
def calculateMinCostDP(s, d):
    minCost[0] = 0
    minCost[1] = cost[0][1]
    
    for i in range(2, d):
        minCost[i] = cost[0][i]
        for i in range(1, i):
            minCost[i] = min(minCost[i], minCost[j] + cost[i][j])

    return minCost[d - 1]

# 6.1
def longestSubstringSum(num: str):
    