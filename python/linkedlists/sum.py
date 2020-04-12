
from node import Node

def addReverse(l1: Node, l2: Node) -> Node:
  dummy = curr = Node(0)
  carry = 0

  while l1 or l2 or carry:
    if l1:
      carry += l1.val
      l1 = l1.next
    if l2:
      carry += l2.val
      l2 = l2.next
    
    curr.next = Node(carry % 10)
    curr = curr.next
    carry = carry // 10

  return dummy.next
