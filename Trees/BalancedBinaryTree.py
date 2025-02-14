def isBalanced(root) -> bool:
    if not root:
        return True
    def maxDepth(node):
        return 0 if not node else 1 + max(maxDepth(node.left), maxDepth(node.right))
    return abs(maxDepth(root.left) - maxDepth(root.right)) <= 1 and isBalanced(root.left) and isBalanced(root.right)