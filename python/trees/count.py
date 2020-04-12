from treenode import TreeNode

# Both iterative and recursive are O(n), O(n)
def count(root: TreeNode) -> int:
  if not root:
    return 0
  return 1 + count(root.left) + count(root.right)

def countIterative(root: TreeNode) -> int:
  if not root:
    return 0

  count = 0
  q = [root]
  while q:
      node = q.pop(0)

      count += 1
      
      if node.left:
          q.append(node.left)
      if node.right:
          q.append(node.right)
  
  return count

# Complete Binary Tree count: (logN)^2
def depth(root: TreeNode) -> int:
  if not root:
    return 0
  return 1 + depth(root.left)

def exists(idx: int, depth: int, node: TreeNode) -> bool:
  left, right = 0, 2 ** depth - 1

  for _ in range(depth):
    pivot = left + (right - left) // 2

    if idx < pivot:
      node = node.left
      right = pivot
    else:
      node = node.right
      left = pivot + 1
  return node is not None


def countComplete(root: TreeNode) -> int:
  if not root:
    return 0
  
  d = depth(root.left)

  left, right = 0, 2 ** depth - 1
  while left <= right:
    pivot = left + (right - left) // 2
    if exists(pivot, d, root):
      left = pivot + 1
    else:
      right = pivot - 1

  return 2 ** d - 1 + left