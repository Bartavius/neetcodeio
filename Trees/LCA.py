# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        

        # BST
        # there are two cases:
            # binary tree splits (2)
            # binary tree has one descendent

        # (both on the condition that the descendents aren't p or q)
        # if binary tree has one descendent, update root to that descendent
        # if binary tree has a split, then update the root 

        # if p or q is found (one of them is descendent of node then return root)
        # also given the condition that their subtrees DO exist, can return root
        # upon discovery that descendent is p or q


        LCA = root

        while LCA:

            if p.val > LCA.val and q.val > LCA.val:
                LCA = LCA.right
            elif p.val < LCA.val and q.val < LCA.val:
                LCA = LCA.left
            else:
                return LCA
        return None