from node import Node

# O(n), O(1)
def kthToLast(head: Node, k: int) -> Node:
  if not head:
    return k
  
  fast = head
  i = 0
  while i < k:
    fast = fast.next
    i += 1
  
  cur = head

  while fast:
    cur = cur.next
    fast = fast.next

  return cur.val

# O(n), O(n)
def kthToLastRecursive(head: Node, k: int, count: int) -> Node:
  if not head:
    return 0

  node = kthToLastRecursive(head.next, k, count)
  count += 1

  if count == k:
    return head
  return node