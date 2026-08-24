# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         if root is not None:
#             print(root.val)
#             self.preorderTraversal(root.left)
#             self.preorderTraversal(root.right)

#             return root

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
        # result = []
        # if not root:
        #     return []
        
        # else:
        #     return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)

        # else:
        #     while root:
        #         result.append(root.val)
        #         self.preorderTraversal(root.left)
        #         self.preorderTraversal(root.right)
        #     return result
