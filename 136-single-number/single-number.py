class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        temp=0
        for i in nums:
            temp^=i
        return temp