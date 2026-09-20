class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        checked={}
        for i in range(len(nums)):
            check=target-nums[i]
            if check in checked:
                return [checked[check],i]
            checked[nums[i]]=i