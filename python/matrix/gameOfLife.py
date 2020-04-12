from typing import List

# Game of life without using extra space: O(n^2), O(1)
def gameOfLife(board: List[List[int]]) -> None:
  rows = len(board)
  cols = len(board[0])
  neighbors = [(1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1)]

  for i in range(rows):
    for j in range(cols):
      count = 0
      for neighbor in neighbors:
        r = i + neighbor[0]
        c = j + neighbor[1]

        if (r < rows and r >= 0) and (c < cols and c >= 0) and abs(board[r][c]) == 1:
          count += 1

      if board[i][j] == 1 and (count < 2 or count > 3):
        board[i][j] = -1
      
      if board[i][j] == 0 and count == 3:
        board[i][j] = 2

  for i in range(rows):
    for j in range(cols):
      if board[i][j] > 0:
        board[i][j] = 1
      else:
        board[i][j] = 0

board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
print(board)
gameOfLife(board)
print(board)

assert board == [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]