cache={}
class Solution:
    def fib(self, n: int) -> int:
        global cache
        if n==1 or n==0:
            return n
        if n in cache:
            return cache[n]
        cache[n]=self.fib(n-1)+self.fib(n-2)
        return cache[n]