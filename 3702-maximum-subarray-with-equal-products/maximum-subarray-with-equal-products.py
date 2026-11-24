import math
from typing import List


class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 1  # Any single positive integer subarray is valid (prod == gcd == lcm)

        for i in range(n):
            prod = nums[i]
            g = nums[i]
            l = nums[i]

            for j in range(i + 1, n):
                x = nums[j]
                prod *= x
                g = math.gcd(g, x)
                l = math.lcm(l, x)

                if prod == l * g:
                    ans = max(ans, j - i + 1)

        return ans