cache={}
class Solution:
    def fib(self, n: int) -> int:
        # global cache
        # if n==1 or n==0:
        #     return n
        # if n in cache:
        #     return cache[n]
        # cache[n]=self.fib(n-1)+self.fib(n-2)
        
        # return cache[n]
        
        dp=[0]*(n+1) 
        if n<=1:
            return n
        dp[1]=1
        for i in range(2, n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n]