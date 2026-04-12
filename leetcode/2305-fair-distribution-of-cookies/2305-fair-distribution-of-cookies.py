class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        c = k * [0]
        res = float('inf')

        def backTrack(n):
            nonlocal res, c
            if n == len(cookies):
                res = min(res, max(c))
                return 
            if res <= max(c):
                return
            for j in range(k):
                c[j] += cookies[n]
                backTrack(n+1)
                c[j] -= cookies[n]
        backTrack(0)
        return res



