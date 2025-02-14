def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    def maxDepth(root):
        return 0 if not root else max(1 + maxDepth(root.left), 1 + maxDepth(root.right))

    return max(maxDepth(root.left) + maxDepth(root.right), self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))