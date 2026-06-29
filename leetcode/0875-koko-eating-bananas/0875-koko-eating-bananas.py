class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def bananas(n):
            ans = 0
            for p in piles:
                ans += ceil(p/n)
            return ans
        low, high = 1, max(piles)
        ans = high
        while low <= high:
            mid = (low + high)//2
            if bananas(mid) > h:
                low = mid + 1
            else:
                high = mid-1
                ans = min(ans, mid)
        return ans
