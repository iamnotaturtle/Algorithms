from node import Node

# Merge two linked lists (unsorted) O(n), O(1)
def mergeUnsortedLists(l1: Node, l2: Node) -> Node:
  if not l1 or not l2:
    return l2 or l1

  head = l1

  while l1.next != None:
    l1 = l1.next
  l1.next = l2

  return head