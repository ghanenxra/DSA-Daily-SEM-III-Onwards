from functools import lru_cache

class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        # Total path length is m + n - 1. A valid bracket sequence must have an even length.
        if (m + n - 1) % 2 != 0:
            return False
        
        # A valid sequence must start with '(' and end with ')'
        if grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False
        
        max_open = (m + n - 1) // 2

        @lru_cache(None)
        def dfs(r: int, c: int, balance: int) -> bool:
            # If open brackets drop below 0 or exceed half the total path length, it cannot be valid
            if balance < 0 or balance > max_open:
                return False
            
            # Reached destination
            if r == m - 1 and c == n - 1:
                return balance == 0
            
            # Explore down and right
            for nr, nc in ((r + 1, c), (r, c + 1)):
                if nr < m and nc < n:
                    delta = 1 if grid[nr][nc] == '(' else -1
                    if dfs(nr, nc, balance + delta):
                        return True
            
            return False

        return dfs(0, 0, 1)