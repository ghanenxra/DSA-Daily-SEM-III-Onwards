# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        inorder = []
        if root is None:
            return []
        def inorder_list(node):
            if node is None:
                return
            inorder_list(node.left)
            inorder.append(node)
            inorder_list(node.right)
            
        def correct_tree(left, right):
            if left>right:
                return None

            mid = (left+right)//2
            present=inorder[mid]
            present.left = correct_tree(left, mid-1)
            present.right = correct_tree(mid+1, right)            
            return present

        inorder_list(root)
        return correct_tree(0, len(inorder)-1)

            
            
        
        