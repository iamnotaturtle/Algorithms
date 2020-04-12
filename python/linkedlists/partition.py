from node import Node

# Rearrange list based on value
def partition(node: Node, value: int) -> Node:
  head: Node = node
  tail: Node = node

  while node:
    nextNode: Node = node.next
    
    if node.val < value:
      node.next = head
      head = node
    else:
      tail.next = node
      tail = node

    node = nextNode

  # End the list
  tail.next = None