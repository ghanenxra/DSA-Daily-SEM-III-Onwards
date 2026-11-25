from collections import Counter
from typing import List


class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return n

        base1, mod1 = 1315423911, 1_000_000_007
        base2, mod2 = 2654435761, 1_000_000_009

        min_val = min(nums)
        vals = [x - min_val + 1 for x in nums]

        pow1 = [1] * (n + 1)
        pow2 = [1] * (n + 1)
        pref1 = [0] * (n + 1)
        pref2 = [0] * (n + 1)

        for i, v in enumerate(vals):
            pow1[i + 1] = (pow1[i] * base1) % mod1
            pow2[i + 1] = (pow2[i] * base2) % mod2
            pref1[i + 1] = (pref1[i] * base1 + v) % mod1
            pref2[i + 1] = (pref2[i] * base2 + v) % mod2

        def get_hash(l: int, r: int) -> tuple[int, int]:
            length = r - l
            h1 = (pref1[r] - pref1[l] * pow1[length]) % mod1
            h2 = (pref2[r] - pref2[l] * pow2[length]) % mod2
            return h1, h2

        def has_unique_of_length(k: int) -> bool:
            counts = Counter(get_hash(i, i + k) for i in range(n - k + 1))
            return any(freq == 1 for freq in counts.values())

        lo, hi = 1, n
        ans = n
        while lo <= hi:
            mid = (lo + hi) // 2
            if has_unique_of_length(mid):
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1

        return ans