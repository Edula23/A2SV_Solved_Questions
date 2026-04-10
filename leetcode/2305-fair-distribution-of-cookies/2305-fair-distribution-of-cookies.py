class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        minUnf = float('inf')
        dist = [0] * k

        def backTrack(i):
            nonlocal minUnf, dist

            if i == len(cookies):
                minUnf = min(minUnf, max(dist))
                return
            if minUnf <= max(dist):
                return 
            for j in range(k):
                dist[j] += cookies[i]
                backTrack(i+1)
                dist[j] -= cookies[i]
        backTrack(0)
        return minUnf
        