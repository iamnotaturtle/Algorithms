# Given sorted array, create BST with minimal height
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def createBST(arr):
    if not arr:
        return
    mid = len(arr) // 2

    node = Node(arr[mid])
    if mid == 0:
        return node

    node.left = createBST(arr[:mid])
    node.right = createBST(arr[mid + 1:])

    return node

def inorder(node, path = []):
    if not node:
        return
    inorder(node.left, path)
    path.append(node.val)
    inorder(node.right, path)

arr = [1, 2, 3, 4, 5]
tree = createBST(arr)

path = []
inorder(tree, path)
assert(path == arr)
