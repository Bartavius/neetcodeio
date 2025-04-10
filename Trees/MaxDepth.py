''' 
Given the root of a binary tree, return its depth.

The depth of a binary tree is defined as the number of nodes along the longest path from the root node down to the farthest leaf node.
'''
def maxDepth(root) -> int:
        return 0 if not root else max(1 + maxDepth(root.left), 1 + maxDepth(root.right))