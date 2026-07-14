def isSameTree(p, q):
    # Both are None
    if not p and not q:
        return True
        
    # One is None, other is not
    if not p or not q:
        return False
        
    # Data not same
    if p.data != q.data:
        return False
        
    # Check left and right subtree
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
def isMirror(t1, t2):
    # Both are None
    if not t1 and not t2:
        return True
        
    # One is None, other is not
    if not t1 or not t2:
        return False
        
    # Data not same or subtrees not mirror
    return (t1.data == t2.data) and \
           isMirror(t1.left, t2.right) and \
           isMirror(t1.right, t2.left)

def isSymmetric(root):
    if not root:
        return True
    return isMirror(root.left, root.right)
