class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        
        divisors = [[] for _ in range(n + 1)]
        for length in range(1, n + 1):
            for d in range(1, length):
                if length % d == 0:
                    divisors[length].append(d)

        def get_palindrome_changes(sub):
            changes = 0
            left, right = 0, len(sub) - 1
            while left < right:
                if sub[left] != sub[right]:
                    changes += 1
                left += 1
                right -= 1
            return changes

        cost = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            for j in range(i, n):
                length = j - i + 1
                min_c = float('inf')
                sub_str = s[i:j+1]
                
                for d in divisors[length]:
                    current_cost = 0
                    for start in range(d):
                        group = sub_str[start::d]
                        current_cost += get_palindrome_changes(group)
                    min_c = min(min_c, current_cost)
                
                cost[i][j] = min_c


        dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
        
        for i in range(n):
            dp[i][1] = cost[i][n - 1]

        for parts in range(2, k + 1):
            for i in range(n - parts + 1):
                for x in range(i, n - parts + 1):
                    dp[i][parts] = min(dp[i][parts], cost[i][x] + dp[x + 1][parts - 1])

        return dp[0][k]