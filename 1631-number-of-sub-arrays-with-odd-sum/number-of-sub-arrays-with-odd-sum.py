class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        m=10**9+7
        odd=0
        even=1
        current=0
        ans=0

        for num in arr:
            current+=num

            if current%2==1:
                ans+=even
                odd+=1
            else:
                ans+=odd
                even+=1
            ans%=m
        return ans