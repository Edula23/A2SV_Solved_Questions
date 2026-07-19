class Solution:
    def fib(self, n: int) -> int:
        memo = {}
        def fibb(n):
            if n <= 1:
                return n
            if n not in memo:
                memo[n] = fibb(n-1) + fibb(n-2)
            
            return memo[n]
        return fibb(n)