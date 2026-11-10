class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        dp=[float('inf')]*(n+1)
        dp[0]=0
        for j in range(1, n+1):
            for i in range(max(0,j-3),j):
                current_cost=dp[i]+costs[j-1]+(j-i)**2
                dp[j]=min(dp[j],current_cost)
        return dp[n]



        # # amount=0
        # dp=[0]*(n+1)
        # dp[0]=0
        # for i in range(2,n+1):
        #     dp[i]=min(dp[i-1]+costs[i-1]+1,dp[i-2]+costs[i-2]+4,dp[i-3]+costs[i-3]+9)
        # return dp[n]