from treenode import TreeNode

# Insertion BST, O(n) (if not balanced)
def insert(root: TreeNode, val: int) -> TreeNode:
  if not root:
    return TreeNode(val)
  elif val < root:
    root.left = insert(root.left, val)
  else:
    root.right = insert(root.right, val)
  return root

# Search BST, O(n) same reason as above
def search(root: TreeNode, val: int) -> TreeNode:
  if not root or root.val == val:
    return root
  elif val < root.val:
    return search(root.left, val)
  else:
    return search(root.right, val)

# Remove BST, O(n)
def remove(root: TreeNode, target: TreeNode) -> None:
  return

# Returns parent of target node
# Use to find successor of node
def findParent(root: TreeNode, target: TreeNode) -> TreeNode:
  if root == target:
    return None

  while root.left != target and root.right != target:
    if target.val < root.val:
      root = root.left
    else:
      root = root.right
  return root

def findSuccessor(root: TreeNode, target: TreeNode) -> TreeNode:
  successor = target.right

  # Find leftmost child of right node
  if successor:
    while successor.left:
      successor = successor.left
    return successor
  
