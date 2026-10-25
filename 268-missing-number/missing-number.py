class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n=len(nums)
        summ=0
        for i in range(0, n+1):
            summ+=i
        return summ-sum(nums)
