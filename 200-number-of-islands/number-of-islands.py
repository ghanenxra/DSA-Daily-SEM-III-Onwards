class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        row, col=len(grid), len(grid[0])
        islands=0

        def dfs(ros , cols):
            if ros<0 or ros>=row or cols<0 or cols>=col or grid[ros][cols]=="0":
                return 
            grid[ros][cols]="0"

            dfs(ros+1, cols)
            dfs(ros-1,cols)
            dfs(ros,cols+1)
            dfs(ros,cols-1)

        for ros in range(row):
            for cols in range(col):
                if grid[ros][cols]=="1":
                    islands+=1
                    dfs(ros,cols)

        return islands

