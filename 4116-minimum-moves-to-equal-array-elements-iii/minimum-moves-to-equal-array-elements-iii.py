class Solution:
    def minMoves(self, nums: List[int]) -> int:
        count=0
        temp=max(nums)
        for x in nums:
            count+=temp-x
        return count