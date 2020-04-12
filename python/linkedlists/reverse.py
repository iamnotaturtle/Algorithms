from node import Node

# Time: O(n), Space: O(n), because of recursion
def reverseRecursive(head: Node):
  if head is None or head.next is None:
    return head
  
  newHead = reverseRecursive(head.next)
  head.next.next = head
  head.next = None
  return newHead

# Time: O(n), Space: O(1)
def reverseIterative(head: Node):
  if head is None or head.next is None:
    return head
  
  prev = None
  curr = head

  while curr is not None:
    curr.next, curr, prev = prev, curr.next, curr

  return prev