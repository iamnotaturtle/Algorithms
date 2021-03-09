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

## MinCost functions
# Regular recursive -> memoized -> dp
# 4.2 Example
# Between s and d, cost of s < i < d is minCost(s, i) + minCost(i, d)
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

# https://tutorialspoint.dev/data-structure/graph-data-structure/find-the-minimum-cost-to-reach-a-destination-where-every-station-is-connected-in-one-direction
def minCost(cost):
    n = len(cost)
    dist = [float('Inf')] * n
    dist[0] = 0

    for i in range(n):
        for j in range(i + 1, n):
            if dist[j] > dist[i] + cost[i][j]:
                dist[j] = dist[i] + cost[i][j]
    
    return dist[-1]

INF = float('Inf')
cost= [ [0, 15, 80, 90], 
        [INF, 0, 40, 50], 
        [INF, INF, 0, 70], 
        [INF, INF, INF, 0]
        ] 
print("The Minimum cost to reach station ", len(cost), " is ", minCost(cost))

# 6.1
def longestSubstringUnoptimized(num):
    n = len(num)
    maxLen = 0

    for i in range(n):
        # Iterate over even substring
        for j in range(i + 1, n, 2):
            length = j - i + 1
            if maxLen > length:
                continue

            # Calculate sum of left and right substrings
            lSum, rSum = 0, 0
            for k in range(length // 2):
                lSum += int(num[i + k])
                rSum += int(num[i + k + length // 2])
            if lSum == rSum:
                maxLen = length
    return maxLen

# 6.5
def longestSubstringDP(num):
    n = len(num)
    maxLen = 0

    # Fill in diagonal (lower half not used)
    s = [[0] * n for i in range(n)]
    for i in range(n):
        s[i][i] = int(num[i])
    
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            k = length // 2
            s[i][j] = s[i][j - k] + s[j - k + 1][j]

            if length % 2 == 0 and s[i][j - k] == s[j - k + 1][j] and length > maxLen:
                maxLen = length
    return maxLen
print("Longest substring DP", longestSubstringDP("142124"))

# https://hackerranksolutionc.blogspot.com/2017/06/longest-even-length-substring-solution.html
def longestSubstringSumOptimized(num: str):
    n = len(num)
    length = 0

    for i in range(n - 1):
        left, right = i, i + 1
        leftSum, rightSum = 0, 0

        while right < n and left >= 0:
            leftSum += int(num[left])
            rightSum += int(num[right])

            if leftSum == rightSum:
                length = max(length, right - left + 1)
            left -= 1
            right += 1

    return length

print("Longest substring", longestSubstringSumOptimized("142124"))

# 7.2
# Given binary tree, add sum of nodes in hierarchy to its value
def sumOfNodes(node):
    if not node or not (node.left and node.right):
        return

    sumOfNodes(node.left) if node.left else None
    sumOfNodes(node.right) if node.right else None

    # Post order traversal
    node.val += node.left.val if node.left else 0
    node.val += node.right.val if node.right else 0

# 7.3
# pascal's triangle
def combination(n, m):
    if n == 0 or m == 0 or n == m:
        return 1
    
    return combination(n - 1, m) + combination(n - 1, m - 1)
def nthRow(n):
    row = [0] * (n + 1)
    row[0] = 1

    for i in range(n + 1):
        for j in range(i, 0, -1):
            row[j] += row[j - 1]
    
    return row

print('Pascal triangle, row 5 is: ', nthRow(5))

# 8.1
def minPathSum(cost):
    if not cost:
        return

    m, n = len(cost), len(cost[0])

    for row in range(m):
        for col in range(n):
            if row == 0 and col > 0:
                cost[row][col] += cost[row][col - 1]
            elif col == 0 and row > 0:
                cost[row][col] += cost[row - 1][col]
            elif row > 0 and col > 0:
                cost[row][col] += min(cost[row - 1][col], cost[row][col - 1])
                cost[row][col] += min(cost[row - 1][col - 1], cost[row - 1][col], cost[row][col - 1]) # Q 8.1, min path sum but diagonal

    return cost[m - 1][n - 1]

# 8.2
# 2 x n plot of land
# similar to fib
def waysToPlaceTile(n):
    if n < 2:
        return 0
    if n == 1 or n == 2:
        return n
    
    return waysToPlaceTile(n - 1) + waysToPlaceTile(n - 2)

# 8.2 3xn plot of land

# 8.3
# 3, 5, 10 points in one move
def waysToScore(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    
    return waysToScore(n - 10) + waysToScore(n - 5) + waysToScore(n - 3)

print("Ways to score for total 13 is", waysToScore(13))

# bottom up
def waysToScoreOptimized(n):
    arr = [0] * (n + 1)
    arr[0] = 1

    for i in range(1, n + 1):
        if i - 3 >= 0:
            arr[i] += arr[i - 3]
        if i - 5 >= 0:
            arr[i] += arr[i - 5]
        if i - 10 >= 0:
            arr[i] += arr[i - 10]
    return arr[-1]
    
print("optimized", waysToScoreOptimized(13))

# 8.4 kadane's
# M(n) = max(M(n - 1) + A[n], A[n])

# 9.1 Edit Distance O(n^3)
def minDistance(str1, str2):
    if not str1:
        return len(str2)
    if not str2:
        return len(str1)

    if str1[0] == str2[0]:
        return minDistance(str1[1:], str2[1:])

    delete = minDistance(str1[1:], str2)
    replace = minDistance(str2[0] + str1[1:], str2)
    insert = minDistance(str2[0] + str1, str2)

    return min(delete, replace, insert) + 1

print('---Edit Distance---')
print(minDistance('cat', 'car'))
print(minDistance('sunday', 'saturday'))

# 9.1 bottom up, O(mn)
# Can furhter optimize by using only 1d array
def minDistanceOptimized(str1, str2):
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, n + 1):
        dp[0][i] = i
    
    for i in range(1, m + 1):
        dp[i][0] = i

    for row in range(1, m + 1):
        for col in range(1, n + 1):
            if str1[row - 1] == str2[col - 1]:
                dp[row][col] = dp[row - 1][col - 1]
            else:
                dp[row][col] = 1 + min(dp[row - 1][col - 1], dp[row - 1][col], dp[row][col - 1])

    return dp[-1][-1]

print('---Edit Distance Optimized ---')
print(minDistanceOptimized('cat', 'car'))
print(minDistanceOptimized('sunday', 'saturday'))

