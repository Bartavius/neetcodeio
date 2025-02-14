'''
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.
'''
def isSubtree(root, subRoot) -> bool:
    stack = [root]

    def candidate(node, subRoot):
        if (node and not subRoot) or (not node and subRoot):
            return False
        if not node and not subRoot:
            return True
        return node.val == subRoot.val and candidate(node.left, subRoot.left) and candidate(node.right, subRoot.right)

    while stack:
        node = stack.pop()
        if node.val == subRoot.val:
            same = candidate(node, subRoot)
            if same:
                return True
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return False