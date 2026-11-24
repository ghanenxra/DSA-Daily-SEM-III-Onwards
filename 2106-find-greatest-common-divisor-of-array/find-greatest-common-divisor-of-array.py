class Solution:
    def findGCD(self, nums: list[int]) -> int:
        low=min(nums)
        high=max(nums)
        ans=1
        i=1
        while i<=low:
            if (low%i==0 and high%i==0):
                ans=i
            i+=1
        return ans
