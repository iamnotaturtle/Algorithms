# OO question
# Design elevator
# * Up/Down efficiently (no priority for now)
# * Users can call elevator from diff floors
from queue import PriorityQueue
import logging, sys

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

UP = 1
DOWN = -1

class Elevator:
    def __init__(self, floors):
        self.direction = UP
        self.floors = floors
        self.current = 0

        # Two queues
        # One for processing incoming calls
        # Another for any inner calls
        # Direction is priorirty: +1/-1 up/down
        self.callq = { i: PriorityQueue() for i in range(floors) }
        self.destinationq = { i: PriorityQueue() for i in range(floors) }

    def move(self):
        if self.current == 0 and self.direction == DOWN or self.current == self.floors and self.direction == UP:
            self.direction *= -1
        
        logging.debug(f" Moving from {self.current} to {self.current + self.direction}")

        self.current += self.direction
        self.processRequests()

    # Handle any requests
    def processRequests(self):
        # Handle any requests from inside the elevator first
        count = 0
        while self.destinationq[self.current]:
            count += 1
            self.destinationq[self.current].pop()
        logging.debug(f"Let {count} user(s) out on floor: {floor}")

        # Handle any external requests if we are on the same floor
        # If we are going down, pickup any requests which are going down
        if self.callq[self.current] and self.callq[self.current][-1][0] == self.direction:

        return

    # Call elevator to floor
    def call(self, direction, floor):
        assert(0 <= floor < self.floors)
        assert(direction == UP or direction == DOWN)

        self.callq[self.current].put((direction, floor))
    
    # Request destination once inside elevator
    def request(self, target):
        assert(0 <= target < self.floors)
 
        if target == self.current:
            return
        
        item = (1 if target - self.current > 0 else -1, target)

        logging.debug(f" Requesting elevator to target: {item[1]} with direction {item[0]}")

        self.destinationq[target].put(item)

    # Pop off any destination requests for the current floor
    def processInternal(self):
        self.destinationq[self.current].pop()


e = Elevator(8)
e.request(1)
e.request(2)
for i in range(16):
    e.move()