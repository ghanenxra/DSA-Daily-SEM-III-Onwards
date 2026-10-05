# cache={}
class Solution:
    def climbStairs(self, n: int) -> int:
        # global cache
        # if n==1 or n==2:
        #     return n
        # if n in cache:
        #     return cache[n]
        # cache[n] = self.climbStairs(n-1)+self.climbStairs(n-2)
        # return cache[n]

        # dp=[0]*n
        if n<=2:
            return n
        dp=[0]*(n+1)
        dp[0]=0
        dp[1]=1
        dp[2]=2

        for i in range(3, n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[i]