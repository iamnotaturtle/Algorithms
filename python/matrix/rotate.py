from typing import List

# Rotate n x n matrix
# O(n^2), O(1)
def rotate(matrix: List[List[int]]) -> None:
  n = len(matrix[0])

  for row in range(n // 2 + n % 2):
    for col in range(n // 2):
      tmp = matrix[n - 1 - col][row]
      matrix[n - 1 - col][row] = matrix[n - 1 - row][n - 1 - col]
      matrix[n - 1 - row][n - 1 - col] = matrix[col][n - 1 - row]
      matrix[col][n - 1 - row] = matrix[row][col]
      matrix[row][col] = tmp

matrix = [[1,2,3],[4,5,6],[7,8,9]]
rotate(matrix)
print(matrix)