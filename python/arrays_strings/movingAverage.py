""" 
  Keeps track of a rolling window of averages
  O(1), O(1)
"""
class MovingAverage:
  def __init__(self, size: int):
    self.window = [0 for i in range(size)]
    self.n = 0
    self.insert = 0
    self.sum = 0

  def next(self, val: int):
    if self.n < len(self.window):
      self.n += 1
    
    self.sum -= self.window[self.insert]
    self.sum += val

    self.window[self.insert] = val
    self.insert = (self.insert + 1) % len(self.window)

    return self.sum / self.n


m = MovingAverage(3)
print(m.next(1) == 1)
print(m.next(10) == (1 + 10) / 2)
print(m.next(3) == (1 + 10 + 3) / 3)
print(m.next(5) == (10 + 3 + 5) / 3)
