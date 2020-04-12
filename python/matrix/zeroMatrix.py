from typing import List

# Sets row col to zero if zero
def setZero(matrix: List[List[int]]) -> None:
  if not matrix or not matrix[0]:
    return
  
  isRowZero = False
  isColZero = False

  # Find zeroes
  for i in range(len(matrix)):
    for j in range(len(matrix[0])):
      val = matrix[i][j]

      if i == 0 and j == 0 and val == 0:
        isRowZero = True
        isColZero = True
      elif i == 0 and val == 0:
        isRowZero = True
      elif j == 0 and val == 0:
        isColZero = True
      elif val == 0:
        matrix[i][0] = 0
        matrix[0][j] = 0
  
  # Zero out matrix
  for i in range(1, len(matrix)):
    for j in range(1, len(matrix[0])):
      if matrix[i][0] == 0 or matrix[0][j] == 0:
        matrix[i][j] = 0
  
  # Zero out first row or col
  if isRowZero:
    for i in range(0, 1):
      for j in range(len(matrix[0])):
        matrix[i][j] = 0
  if isColZero:
    for i in range(len(matrix)):
      for j in range(0, 1):
        matrix[i][j] = 0

matrix = [[1,1,1],[1,0,1],[1,1,1]]
setZero(matrix)
assert matrix == [[1,0,1],[0,0,0],[1,0,1]]