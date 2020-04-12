# Inorder traversal with O(1) space
from treenode import TreeNode

def inorder(root):
    res = []
    if not root:
        res
    
    cur = root
    while cur:
        if not cur.left:
            res.append(cur.val)
            cur = cur.right
        else:
            # Find predecessor
            prev = cur.left
            while prev and prev.right != cur:
                prev = prev.right
            
            if not prev.right:
                prev.right = cur
                cur = cur.left
            else:
                prev.right = None
                res.append(cur.val)
                cur = cur.right

    return res