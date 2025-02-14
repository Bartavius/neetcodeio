'''
You are given the root of a binary tree root. Invert the binary tree and return its root.
'''
def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    if root:
        stack = [root]
        while stack:
            node = stack.pop()
            node.left, node.right = node.right, node.left
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

    return root