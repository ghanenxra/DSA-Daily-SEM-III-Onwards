class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()
        dp={}
        temp=0

        for i in nums:
            change_val=i+1
            dp[change_val]=dp.get(i,0)+1

            if dp[change_val]>temp:
                temp=dp[change_val]

            dp[i]=dp.get(i-1,0)+1

            if dp[i]>temp:
                temp=dp[i]

        return temp