class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        dp=[0]*(n+1)

        for i in range(2, n+1):
            dp[i]=min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])

        return dp[n]



        # n=len(cost)
        # dp=[0]*(n+1)
        # def less_cost(i):
        # #     if i<=1:
        # #         return cost[i]
        # #     if i in cache:
        # #         return cache[i]

        # #     cache[i]=cost[i]+min(less_cost(i-1), less_cost(i-2))
        # #     return cache[i]
        # # return min(less_cost(n-1), less_cost(n-2))

        
        #     dp[1]=cost[0]
        #     dp[2]=cost[1]

        #     dp[i]=cost[i]+min(dp[i-1], dp[i-2])
        #     return dp[i]
        
        
        # def min_cost(i):
        #     n=len(cost)
        #     if i<=1:
        #         return cost[i]
        #     return cost[i]+min(min_cost(i-1), min_cost(i-2))
        # return min(min_cost(n-1), min_cost(n-2))