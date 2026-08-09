from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()  # Stores indices
        res = []

        for i in range(len(nums)):
            # 1. Remove indices outside the current window range [i - k + 1, i]
            if dq and dq[0] <= i - k:
                dq.popleft()

            # 2. Maintain decreasing order in deque
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()

            # 3. Add current index
            dq.append(i)

            # 4. Append max element to result once window reaches size k
            if i >= k - 1:
                res.append(nums[dq[0]])

        return res
        # ans = []
        # queue = []
        # for i in range(k):
        #     queue.append(nums[i])
        # ans.append(max(queue))

        # for i in range(k,len(nums)):
        #     if len(queue) == k: queue.pop(0)
        #     queue.append(nums[i])
        #     ans.append(max(queue))

        # return ans