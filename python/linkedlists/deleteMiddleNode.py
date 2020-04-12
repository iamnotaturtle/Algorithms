from node import Node

# O(n), O(1)
def delete(node: Node) -> None:
  if not node or not node.next:
    return
  
  nextNode = node.next
  node.val = nextNode.val
  node.next = nextNode.next
