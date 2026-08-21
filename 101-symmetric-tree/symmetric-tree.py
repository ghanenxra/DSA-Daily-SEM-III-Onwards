# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def equal_check(l, r):
            if l is None and r is None:
                return True
            if l is None or r is None:
                return False
            if l.val != r.val:
                return False
            return equal_check(l.left, r.right) and equal_check(l.right, r.left)

        return equal_check(root.left, root.right)






















        # # def symtee(root1, root2):
        #     if root is None:
        #         return True

        #     if root.left is None and root.right is None:
        #         return True

        #     if root.right is None and root.left is not None:
        #         return False

        #     if root.left is None and root.right is not None:
        #         return False

        #     if (self.isSymmetric(root.left.val == root.right.val) == self.isSymmetric(root.right.val,root.left.val)):
        #         return self.isSymmetric(root)






            # if root1 is None and root2 is None:
            #     return True
            # if root1 is None or root2 is None:
            #     return False
            # if root.val != root2.val:
            #     return False
            # return symtee(root1.left, root2.right) and symtee(root1.right, root2.symtee)

        # return symtee(root, root)
