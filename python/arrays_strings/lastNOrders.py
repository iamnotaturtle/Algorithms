# You run an e-commerce website and want to record the last N order ids in a log. Implement a data structure to accomplish this, with the following API:

#     record(order_id): adds the order_id to the log
#     get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.

# You should be as efficient with time and space as possible.
class Log:
    def __init__(self, N):
        self.size = N
        self.q = [None for i in range(self.size)]
        self.current = 0
    
    def record(self, order_id: int):
        self.q[self.current] = order_id
        self.current = (self.current + 1) % self.size
    
    def get_last(self, i: int):
        assert(0 <= i <= self.size)
        return self.q[(self.current - i + self.size) % self.size]

log = Log(3)
log.record(1)
log.record(2)
log.record(3)
assert(log.get_last(1) == 3)

log.record(4)
assert(log.get_last(3) == 2)
