class Solution:
    def fib(self, n: int) -> int:
        # if n == 0:
        #     return 0
        # if n == 1:
        #     return 1

        # first_ele = self.fib(n-1)
        # second_ele = self.fib(n-2)

        # return first_ele + second_ele

        return n if n<=1 else self.fib(n-1)+self.fib(n-2)