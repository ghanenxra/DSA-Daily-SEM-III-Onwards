# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        if root is None:
            return 0
        if root.val>high:
            return self.rangeSumBST(root.left, low, high)
        if root.val<low:
            return self.rangeSumBST(root.right,low, high)
        
        return root.val + self.rangeSumBST(root.left, low, high)+self.rangeSumBST(root.right,low, high)
        










        # ans = []
        # def levelorder(root):
        #     self.inorder(root.left)
        #     ans.append(root.val)
        #     self.inorder(root.right)
        # return ans










            # ans)
            # root.val
            # self.inorder(root.right
            # ans.append(left) 
            # ans.append(mid) 
            # ans.append(right)
        # return (ans)

        # if root is None:
        #     return 0

        