# https://www.dailycodingproblem.com/blog/lockable-binary-trees/
class LockedNode:
    def __init__(self, val = None):
        self.val = val
        self.locked = False
        self.lockedDescendants = 0

        self.right, self.left, self.parent = None, None, None
    
    def isLocked(self) -> bool:
        return self.locked

    def canLockUnlock(self):
        if self.lockedDescendants > 0:
            return False
        
        cur = self.parent
        while cur:
            if cur.locked:
                return False
            cur = cur.parent
        
        return True
    
    def lock(self):
        if self.canLockUnlock():
            self.locked = True
            cur = self.parent
            while cur:
                cur.lockedDescendants += 1
                cur = cur.parent
            return True
        else:
            return False
    
    def unlock(self):
        if self.canLockUnlock():
            self.locked = False

            cur = self.parent
            while cur:
                cur.lockedDescendants -= 1
                cur = cur.parent
            return True
        else:
            return False
        
# Test cases
root = LockedNode(0)

root.left = LockedNode(1)
root.left.parent = root

root.right = LockedNode(2)
root.right.parent = root

root.right.lock()
assert(root.right.isLocked() == True)

root.lock()
assert(root.isLocked() == False)

root.right.unlock()
assert(root.right.isLocked() == False)
