from collections import deque
class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        row=len(grid)
        col=len(grid[0])
        queue=deque()
        fresh=0

        for ros in range(row):
            for cols in range(col):
                if grid[ros][cols]==2:
                    queue.append((ros,cols))
                elif grid[ros][cols]==1:
                    fresh+=1
        
        if fresh==0:
            return 0
        
        time=0
        directions=[(-1, 0),(1, 0), (0,-1), (0, 1)]

        while queue and fresh>0:
            time+=1

            for _ in range(len(queue)):
                ros, cols=queue.popleft()

                for d_ros, d_cols in directions:
                    n_ros, n_cols=ros+d_ros, cols+d_cols
                    if 0<= n_ros<row and 0<=n_cols<col and grid[n_ros][n_cols]==1:
                        grid[n_ros][n_cols]=2
                        fresh-=1
                        queue.append((n_ros, n_cols))

        return time if fresh==0 else -1