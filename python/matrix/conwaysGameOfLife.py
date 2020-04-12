from typing import List
from tkinter import Tk, Canvas
from time import sleep

""" 
For a space that is 'populated':
Each cell with one or no neighbors dies, as if by solitude.
Each cell with four or more neighbors dies, as if by overpopulation.
Each cell with two or three neighbors survives.
For a space that is 'empty' or 'unpopulated'
Each cell with three neighbors becomes populated. 
"""
class GameOfLife:
  def __init__(self, state: List[List[str]], iterations: int, root):
    self.state = state
    self.rows = len(state)
    self.cols = len(state[0])
    self.iterations = iterations
    self.currentIteration = 1

    # GUI
    self.root = root
    self.tiles = [[None for _ in range(self.cols)] for _ in range(self.rows)]
    self.canvas = Canvas(self.root, width=500, height=500, borderwidth=5, background='black')
    self.canvas.pack()

    self.col_width = 20
    self.row_height = 20

  def print(self) -> None:
    print("Iteration - ", self.currentIteration)
    for row in range(self.rows):
      for col in range(self.cols):
        print(self.state[row][col] + " ", end = '')

        # GUI
        if self.state[row][col] == '*':
          x1 = col * self.col_width
          y1 = row * self.row_height
          x2 = x1 + self.col_width
          y2 = y1 + self.row_height
          self.tiles[row][col] = self.canvas.create_rectangle(x1, y1, x2, y2, fill="white")
        else:
          self.canvas.delete(self.tiles[row][col])
          self.tiles[row][col] = None
      print()
    sleep(0.5)
    self.root.update()
    
  def getAliveNeighbors(self, row: int, col: int) -> int:
    count = 0

    # Top
    if row - 1 >= 0 and self.state[row - 1][col] == '*':
      count += 1

    # Bottom
    if row + 1 < self.rows and self.state[row + 1][col] == '*':
      count += 1
      
    # Left
    if col - 1 >= 0 and self.state[row][col - 1] == '*':
      count += 1

    # Right
    if col + 1 < self.cols and self.state[row][col + 1] == '*':
      count += 1
    
    # Diagonal - Top, Left
    if row - 1 >= 0 and col - 1 >= 0 and self.state[row - 1][col - 1] == '*':
      count += 1

    # Diagonal - Top, Right
    if row - 1 >= 0 and col + 1 < self.cols and self.state[row - 1][col + 1] == '*':
      count += 1

    # Diagonal - Bottom, Left
    if row + 1 < self.rows and col - 1 >= 0 and self.state[row + 1][col - 1] == '*':
      count += 1

    # Diagonal - Bottom, Right
    if row + 1 < self.rows and col + 1 < self.cols and self.state[row + 1][col + 1] == '*':
      count += 1

    return count

  def mutate(self) -> None:
    newState = [['-' for col in range(self.cols)] for row in range(self.rows)]

    for row in range(self.rows):
      for col in range(self.cols):

        # Figure out alive neighbors
        neighbors = self.getAliveNeighbors(row, col)

        # If alive
        if self.state[row][col] == '*' and (neighbors == 2 or neighbors == 3):
          newState[row][col] = '*'
        # If dead
        elif self.state[row][col] == '-' and neighbors == 3:
          newState[row][col] = '*'
        # Otherwise the cell dies

    self.print()
    self.currentIteration += 1
    self.state = newState

    if self.currentIteration <= self.iterations:
      self.mutate()


def getState(file: str) -> List[List[str]]:
  state = []

  with open(file) as f:
      for line in f:
        row = []
        chars = list(line)
        
        for c in chars:
          if c == '.':
            row.append('-')
          elif c == 'O':
            row.append('*')

        state.append(row)

  return state

root = Tk()
root.wm_title("Conway's Game of Life")

# Oscillator
# gof = GameOfLife([['-', '-', '-'], ['*', '*', '*'], ['-', '-', '-']], 4, root)


# Pulsar
state = getState('pulsar.cells')
print(len(state), len(state[0]))
gof = GameOfLife(state, 100, root)

root.update()
gof.mutate()
