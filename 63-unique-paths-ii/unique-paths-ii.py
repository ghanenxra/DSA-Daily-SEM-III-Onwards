class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        # dp=[[1]*n for _ in range(m)]
        dp=[0]*n
        dp[0]=1
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j]==1:
                    dp[j]=0
                elif j>0:
                    dp[j]+=dp[j-1]
        return dp[-1]



                # dp[i][j]=dp[i-1][j]+dp[i][j-1]
        # return dp[m][n]