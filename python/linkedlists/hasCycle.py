from node import Node

# Time: O(n), Space: O(1)
def hasCycle(head: Node) -> bool:
  if not head or not head.next:
    return False

  trailing = head
  leading = head.next

  while leading is not None and leading.next is not None:
    if trailing.val == leading.val:
      return True

    trailing = trailing.next
    leading = leading.next.next

  return False
