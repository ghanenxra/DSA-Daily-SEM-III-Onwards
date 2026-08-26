# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if root is None:
            return root
        if root==p or root==q:
            return root
        
        i = self.lowestCommonAncestor(root.left, p, q)
        j = self.lowestCommonAncestor(root.right, p, q)
         
        if i and j:
            return root

        if j:
            return j
        else:
            return i