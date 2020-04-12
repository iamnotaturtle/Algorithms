# Union Find Solution
from typing import List

class Solution:
  def find(self, x: int) -> int:
    if self.parent[x] == x:
      return self.parent[x]
    else:
      return self.find(self.parent[x])

  def union(self, x: int, y: int):
    xRoot, yRoot = self.find(x), self.find(y)

    if xRoot == yRoot:
      return
    
    self.parent[xRoot] = yRoot
    self.count -= 1

  def numOfIslands(self, grid: List[List[int]]) -> int:
    if not grid:
      return 0
  
    rows, cols = len(grid), len(grid[0])
    self.parent = [i for i in range(rows * cols)]
    self.count = sum(grid[i][j] == "1" for i in range(rows) for j in range(cols))

    for i in range(rows):
      for j in range(cols):
        if grid[i][j] == "0":
          continue
        
        idx = i * cols + j

        if j < cols - 1 and grid[i][j + 1] == "1":
          self.union(idx, idx + 1)
        if i < rows - 1 and grid[i + 1][j] == "1":
          self.union(idx, idx + cols)

    return self.count
  
sol = Solution()
assert sol.numOfIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]) == 3