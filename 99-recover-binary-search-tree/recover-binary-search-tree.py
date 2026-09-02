# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        node_val = []
        def inorder_tree(root):
            if root is  None:
                return 
            inorder_tree(root.left)
            node_val.append(root)
            inorder_tree(root.right)

        inorder_tree(root)
        values=[]
        for node in node_val:
            values.append(node.val)
        values.sort()
        for i in range(len(node_val)):
            node_val[i].val=values[i]


        # if root is None:
        #     return None
        # if root.val>root.left.val:
        #     left_sub=self.recoverTree(root.left)
        # if root.val<root.right.val:
        #     right_sub=self.recoverTree(root.right)
