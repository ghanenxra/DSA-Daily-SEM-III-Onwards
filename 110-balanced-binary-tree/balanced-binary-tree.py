# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check_height(node):
            if node is None:
                return 0
            
            left = check_height(node.left)
            right = check_height(node.right)

            if left==-1 or right==-1:
                return -1
            if abs(left-right)>1:
                return -1
            else:
                return max(left, right)+1

        return check_height(root) is not -1















        # if root is None:
        #     return True

        # if root:
        #     self.isBalanced(abs(0<=root.left-root.right<=1))

        