from collections import deque

class Monoqueue:
    def __init__(self, increasing = False):
        self.q = deque()
        self.increasing = increasing

    def push(self, num):
        if self.increasing:
            while self.q and self.q[-1] > num:
                self.q.pop()
        else:
            while self.q and self.q[-1] < num:
                self.q.pop()
        self.q.append(num)
        return
    
    def pop(self) -> int:
        return self.q.popleft()

# Decreasing
mq = Monoqueue()
arr = [5, 3, 1, 2, 4]
for num in arr:
    mq.push(num)
assert(list(mq.q) == [5, 4])

# Increasing
mq = Monoqueue(increasing=True)
arr = [5, 3, 1, 2, 4]
for num in arr:
    mq.push(num)
assert(list(mq.q) == [1, 2, 4])
