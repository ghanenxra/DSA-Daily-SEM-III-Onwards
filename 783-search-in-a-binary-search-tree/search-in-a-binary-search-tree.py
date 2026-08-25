# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        

        if root is None or root.val == val:
            return root

        if val <= root.val:
            return self.searchBST(root.left,val)
        
        else:
            return self.searchBST(root.right,val)
        # child = root
        # child_left = child.left
        # chlid_right = child.right
        # parent = None
        # if root.val >= val:
        #     if root.right.val == val:
        #         return root
        #     else:
        #         self.searchBST(root, val)
        
        # if root.val <= val:
        #     if root.left.val == val:
        #         return root
        #     else:
        #         self.searchBST(root, val)



                
        