from __future__ import annotations
from threading import RLock
from concurrent.futures import ThreadPoolExecutor
from typing import Optional

class Node:
    val: int = None
    nxt: Node = None
    prev: Node = None
    lock = RLock()

class ConcurrentSortedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.nxt = self.tail
        self.tail.prev = self.head

    def __str__(self):
        cur = self.head

        nodes = []
        while cur:
            nodes.append(str(cur.val))
            cur = cur.nxt
        return ' '.join(nodes)

    def insert(self, val: int):
        cur = self.head
        cur.lock.acquire()
        nxt = cur.nxt

        try:
            while True:     
                nxt.lock.acquire()

                try:
                    if nxt == self.tail or nxt.val > val:
                        node = Node()
                        node.val, node.prev, node.nxt = val, cur, nxt
                        nxt.prev = node
                        cur.nxt = node
                        break
                finally:
                    cur.lock.release()
                cur = nxt
                nxt = cur.nxt
        finally:
            nxt.lock.release()
        print(self.__str__())

if __name__ == "__main__":

    # Create sorted list
    lst = ConcurrentSortedList()

    # Create three threads
    with ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(lst.insert, range(1, 4))

