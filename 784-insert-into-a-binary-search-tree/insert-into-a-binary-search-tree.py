# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        new_node = TreeNode(val)
        if root is None:
            return new_node
        
        temp = root
        while temp:
            if temp.val < val:
                if temp.right is None:
                    temp.right = new_node
                    break
                temp = temp.right
            else:
                if temp.left is None:
                    temp.left = new_node
                    break
                temp = temp.left

        return root

        # if root.val > val:
        #     return self.insertIntoBST(root.left,val)
        # else:
        #     return self.insertIntoBST(root.right, val)
