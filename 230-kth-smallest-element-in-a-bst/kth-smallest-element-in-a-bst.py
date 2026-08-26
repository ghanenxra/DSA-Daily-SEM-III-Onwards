# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        ans = []

        def inorder(node):
            if node is None:
                return 
            inorder(node.left)
            ans.append(node.val)
            inorder(node.right)

        inorder(root)
        return ans[k-1]






        # ans =[]
        # if root is None:
        #     return None
        # if root is not None:
        #     ans.append(self.kthSmallest(root.left, k))
        #     ans.append(root.val)
        #     ans.append(self.kthSmallest(root.right,k))

        # return ans