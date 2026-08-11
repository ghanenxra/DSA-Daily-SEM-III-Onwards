class Solution:
    def climbStairs(self, n: int) -> int:
        # if n==0 or n==1:
        #     return 1

        # return self.climbStairs(n-1) + self.climbStairs(n-2)

        if n <= 2:
            return n
        
        prev_step1 = 2
        prev_step2 = 1
        
        for i in range(3, n + 1):
            total_ways = prev_step1 + prev_step2
            prev_step2 = prev_step1
            prev_step1 = total_ways
        
        return prev_step1