class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return max(nums)
        dp=[0]*len(nums)
        dp[0]=nums[0]
        dp[1]=max(nums[0], nums[1])

        for i in range(1, len(nums)):
            dp[i]=max(nums[i]+dp[i-2],dp[i-1])
            # dp[i]=(nums[i]+dp[i-2])
            # dp[i+1]=(nums[i]+dp[i-2])

        return dp[-1]
