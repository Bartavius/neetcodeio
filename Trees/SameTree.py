'''
Given the roots of two binary trees p and q, return true if the trees are equivalent, otherwise return false.

Two binary trees are considered equivalent if they share the exact same structure and the nodes have the same values.
'''
def isSameTree(p, q) -> bool:
    if p and not q or q and not p:
        return False
    if not p and not q:
        return True
        
    current_val = p.val == q.val
    return current_val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
