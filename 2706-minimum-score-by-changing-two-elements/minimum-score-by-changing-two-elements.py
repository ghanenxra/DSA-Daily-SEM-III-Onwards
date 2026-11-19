class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        n=len(nums)
        if n<=3:
            return 0
        
        nums.sort()

        smallest_change=nums[-1]-nums[2]
        largest_change=nums[-3]-nums[0]
        both_change=nums[-2]-nums[1]

        return min(smallest_change, largest_change, both_change)
