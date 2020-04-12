from typing import Dict
from node import Node

# Remove duplicates from unsorted list
# O(n), O(n)
def removeUnsorted(head: Node) -> None:
  if not head:
    return head
  
  hash: Dict[int: bool] = {}

  # Trick here: use previous node set as none instead of next node
  previous = None

  while head:
    if head.val in hash:
      previous.next = head.next.next
    else:
      hash[head.val] = True
      previous = head

    head = head.next
  return head

# Remove duplicates from unsorted list, no buffer
# O(n^2), O(1)
def removeUnsortedNoBuffer(head: Node) -> None:
  if not head:
    return head

  current = head

  while current:
    runner = current
    while runner.next != None:
      if runner.next.val == current.val:
        runner.next = runner.next.next
      else:
        runner = runner.next

    current = current.next
  return head