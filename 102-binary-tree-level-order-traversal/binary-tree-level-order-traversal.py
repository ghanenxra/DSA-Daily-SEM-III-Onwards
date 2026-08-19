# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution(object):
    def levelOrder(self, root):
        ans = []
        if root == None:
            return ans
        queue = deque([root])
        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)
            ans.append(level)

        return ans
        












        # if root.left is None or root.right is None:
        #     return []

        

        


