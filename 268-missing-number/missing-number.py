class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        x=0
        for i in range(len(nums)+1):
            x^=i
        for j in nums:
            x^=j
        return x

         