class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        temp=[]
        for k in range(l,r+1):
            for i in range(len(nums)-k+1):
                window=(sum(nums[i:k+i]))
                if window>0:
                    temp.append(window)
        if len(temp)==0:
            return -1
        return min(temp)