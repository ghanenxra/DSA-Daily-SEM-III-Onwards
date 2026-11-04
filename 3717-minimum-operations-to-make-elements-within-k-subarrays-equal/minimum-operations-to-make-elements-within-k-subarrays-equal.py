from bisect import bisect_left
from typing import List
from sortedcontainers import SortedList


class Solution:

  def minOperations(self, nums: List[int], x: int, k: int) -> int:
    n = len(nums)
    sl = SortedList()
    mid_idx = (x - 1) // 2

    left_sum, right_sum = 0, 0
    cost = [0] * n

    def add(v):
      nonlocal left_sum, right_sum
      pos = sl.bisect_left(v)
      sl.add(v)
      if pos <= mid_idx:
        left_sum += v
        if len(sl) > mid_idx + 1:
          promoted = sl[mid_idx + 1]
          left_sum -= promoted
          right_sum += promoted
      else:
        right_sum += v

    def remove(v):
      nonlocal left_sum, right_sum
      pos = sl.bisect_left(v)
      sl.remove(v)
      if pos <= mid_idx:
        left_sum -= v
        if len(sl) > mid_idx:
          demoted = sl[mid_idx]
          right_sum -= demoted
          left_sum += demoted
      else:
        right_sum -= v

    for i, val in enumerate(nums):
      add(val)
      if i >= x:
        remove(nums[i - x])

      if i >= x - 1:
        med = sl[mid_idx]
        left_cnt = mid_idx + 1
        right_cnt = x - left_cnt
        cost[i] = (left_cnt * med - left_sum) + (right_sum - right_cnt * med)

    dp = [0] * (n + 1)
    for _ in range(k):
      nxt = [float('inf')] * (n + 1)
      for i in range(x - 1, n):
        nxt[i + 1] = min(nxt[i], dp[i + 1 - x] + cost[i])
      dp = nxt

    return dp[n]