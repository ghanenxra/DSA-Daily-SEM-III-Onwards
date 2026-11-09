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