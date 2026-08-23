class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0]*(n+1)
        track_2 = 2
        for i in range(1,n+1):
            if track_2*2 == i:
                dp[i]=1
                track_2=i
        
            else:
                dp[i]=dp[i-track_2]+1
        return dp