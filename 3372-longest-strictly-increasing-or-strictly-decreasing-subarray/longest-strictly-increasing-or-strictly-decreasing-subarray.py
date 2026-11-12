class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        high=1
        low=1
        maxx=1  #this for the base conditionj when there is only one element in the array or only one subarray which is satisfying the condition

        for i in range(1, len(nums)):
            if nums[i]>nums[i-1]:
                high+=1
                low=1
            elif nums[i-1]>nums[i]:
                low+=1
                high=1
            else:
                high=1
                low=1
            maxx=max(low, high, maxx)
        return maxx














        # if len(nums)==1:
        #     return 1
        # num_reverse=nums[::-1]
        # i=0
        # j=1
        # maxx=[]
        # count=0
        # while j!=len(nums):
        #     if nums[i]<nums[j]:
        #         j+=1
        #         count+=1
        #     elif nums[i]>nums[j]:
        #         j=i+1

        # count2=0
        # while j!=len(num_reverse):
        #     if num_reverse[i]<num_reverse[j]:
        #         j+=1
        #         count2+=1
        #     elif num_reverse[i]>num_reverse[j]:
        #         j=i+1

        # maxx.append(count)
        # maxx.append(count2)
        # return max(maxx)
            
