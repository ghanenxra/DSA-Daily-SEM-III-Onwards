class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        mt=[[1]*n for i in range(m)]

        for i in range(1,m):
            for j in range(1, n):
                mt[i][j]=mt[i-1][j]+mt[i][j-1]
        
        return mt[m-1][n-1]


        # count=0
        # if m==0 and n==0:
        #     return 0
        

