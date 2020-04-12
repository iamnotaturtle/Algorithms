from depth import depth
from treenode import TreeNode

# O(n^2) in unbalanced tree
def isBalanced(root: TreeNode) -> bool:
  if not root:
    return True
  if not isBalanced(root.left) or not isBalanced(root.right):
    return False

  return abs(depth(root.left) - depth(root.right)) <= 1

# Optimized: O(n)
def isBalancedOptimized(root: TreeNode) -> bool:
  return dfsHeight(root) != -1

def dfsHeight(root: TreeNode) -> int:
  if not root:
    return 0

  left = dfsHeight(root.left)
  if left == -1:
    return -1

  right = dfsHeight(root.right)
  if right == -1:
    return -1

  if abs(left - right) > 1:
    return -1

  return max(left, right) + 1
