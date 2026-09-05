# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        total_sum=0
        def reverse_inorder(point):
            nonlocal total_sum
            if point is None:
                return 
            reverse_inorder(point.right)
            total_sum+=point.val
            point.val=total_sum
            reverse_inorder(point.left)
        
        reverse_inorder(root)
        return root


        # arr = []


        # def inorder(root):
        #     self.inorder(root.left)
        #     arr.append(root.val)
        #     self.inorder(root.right)
        
        # return 
            