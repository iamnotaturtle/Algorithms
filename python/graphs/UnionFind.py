from typing import List

""" 
Union Find Data Structure
https://github.com/williamfiset/data-structures/blob/master/com/williamfiset/datastructures/unionfind/UnionFind.java
"""
class UnionFind:
  numComponents = 0
  size = 0
  sizes: List[int] = []
  ids: List[int] = []

  def __init__(self, size: int):
    assert size > 0

    self.size = self.numComponents = size
    self.ids = [i for i in range(size)]
    self.sizes = [1] * size

  def find(self, p: int) -> int:
    root = p
    
    # Find the root
    while root != self.ids[root]:
      root = self.ids[root]
    
    # Compress path
    while p != root:
      nxt = self.ids[p]
      self.ids[p] = root
      p = nxt
    
    return root

  def connected(self, p: int, q: int) -> bool:
    return self.find(p) == self.find(q)
  
  def componentSize(self, p: int) -> int:
    return self.sizes[self.find(p)]

  def unify(self, p: int, q: int):
    rootP = self.find(p)
    rootQ = self.find(q)

    if rootP == rootQ: 
      return
    
    if self.sizes[rootP] < self.sizes[rootQ]:
      self.sizes[rootQ] += self.sizes[rootP]
      self.ids[rootP] = rootQ
    else:
      self.sizes[rootP] += self.sizes[rootQ]
      self.ids[rootQ] = rootP

    self.numComponents -= 1

# Test
uf = UnionFind(5)
assert uf.numComponents == 5

uf.unify(0, 1)
assert uf.numComponents == 4
assert uf.componentSize(0) == 2

uf = UnionFind(7)
for i in range(7): assert uf.connected(i, i) == True
