class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        seen=set()
        provinces=0

        def dfs_traversal(entity):
            for i in range(n):
                if isConnected[entity][i]==1 and i not in seen:
                    seen.add(i)
                    dfs_traversal(i)

        
        for i in range(n):
            if i not in seen:
                seen.add(i)
                dfs_traversal(i)
                provinces+=1
        return provinces