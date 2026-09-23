"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if not node:
            return None
        
        cache={}

        def dfs(curr):
            if curr in cache:
                return cache[curr]

            duplicate=Node(curr.val)
            cache[curr]=duplicate

            for neighbor in curr.neighbors:
                duplicate.neighbors.append(dfs(neighbor))
            return duplicate
        return dfs(node)
