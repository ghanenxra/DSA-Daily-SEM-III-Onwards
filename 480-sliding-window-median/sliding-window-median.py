
class Solution:
    def medianSlidingWindow(self, nums: list[int], k: int) -> list[float]:
        ans=[]
        subarray = sorted(nums[:k])

        for j in range(len(nums)-k+1):
            if k%2==0:
                if k>=4:
                    i=k//2
                    temp=(subarray[i-1]+subarray[i])/2
                    ans.append(temp)
                elif k==2:
                    temp=sum(subarray)/2
                    ans.append(temp)
            elif k%2!=0:
                k>=1
                i=k//2
                ans.append(subarray[i])
# The below function is used to prevent the tle by just poping the end element to let the next incoming element inside the subarray  
            if j + k < len(nums):
                outgoing_elem = nums[j]  
                incoming_elem = nums[j + k] 
        
                idx = bisect.bisect_left(subarray, outgoing_elem)
                del subarray[idx]
                bisect.insort(subarray, incoming_elem)
        
        return ans