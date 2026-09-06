cache = {}
class Solution:
    def tribonacci(self, n: int) -> int:
        global cache
        if n==1 or n==2:
            return 1
        if n==0:
            return 0
        if n in cache:
            return cache[n]
        cache[n] = self.tribonacci(n-1)+self.tribonacci(n-2)+self.tribonacci(n-3)
        return cache[n]








        # if n==0 or n==1:
        #     return n
        # if n==2:
        #     return 1

        # return self.tribonacci(n-1)+self.tribonacci(n-2)+self.tribonacci(n-3)