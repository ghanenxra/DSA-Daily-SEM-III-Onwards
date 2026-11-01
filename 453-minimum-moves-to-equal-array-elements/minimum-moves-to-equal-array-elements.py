class Solution:
    def minMoves(self, nums: list[int]) -> int:
        return sum(nums)-len(nums)*min(nums)

        # if len(nums)!=len(set(nums)):
        #     return 0
        # if len(nums)==1:
        #     return 0
        
        # return max(nums)+1-min(nums)