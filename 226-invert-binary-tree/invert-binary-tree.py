# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)


        return root




        # if root is None:
        #     return None
        # if self.root.right is None and self.root.left is None:
        #     return self.root
        # if self.root:
        #     return (self.invertTree(root.left==root.right), self.invertTree(root.right==root.left))