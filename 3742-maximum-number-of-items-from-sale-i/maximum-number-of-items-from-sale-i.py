from typing import List


class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        frees = [0] * n

        # Count free copies unlocked when buying item i at least once
        for i in range(n):
            factor_i = items[i][0]
            cnt = 0
            for j in range(n):
                if i != j and items[j][0] % factor_i == 0:
                    cnt += 1
            frees[i] = cnt

        # dp[b] = max total item copies obtainable with spent budget <= b
        dp = [0] * (budget + 1)

        for i in range(n):
            price = items[i][1]
            free_cnt = frees[i]

            # Step 1: First purchase of item i (0/1 transition -> right to left)
            b = budget
            while b >= price:
                candidate = dp[b - price] + 1 + free_cnt
                if candidate > dp[b]:
                    dp[b] = candidate
                b -= 1

            # Step 2: Additional copies of item i (unbounded -> left to right)
            b = price
            while b <= budget:
                candidate = dp[b - price] + 1
                if candidate > dp[b]:
                    dp[b] = candidate
                b += 1

        return dp[budget]