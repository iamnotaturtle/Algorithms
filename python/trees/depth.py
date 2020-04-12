from treenode import TreeNode

# Recursive depth
def depth(root: TreeNode) -> int:
  if not root:
    return 0
  return 1 + max(depth(root.left), depth(root.right))

# Iterative depth (DFS)
def depthIterative(root: TreeNode) -> int:
  if not root:
    return 0
  
  depth = 0
  stack = [(root, 1)]

  while stack:
    node, level = stack.pop()

    if node:
      depth = max(depth, level)
      stack.append((node.left, level + 1))
      stack.append((node.right, level + 1))
  
  return depth
