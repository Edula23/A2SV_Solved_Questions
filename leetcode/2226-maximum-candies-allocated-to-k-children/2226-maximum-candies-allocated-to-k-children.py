class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        summ = sum(candies)
        if summ < k:
            return 0
        left, right = 1, summ//k
        ans = 0
        while left <= right:
            mid = (left+right)//2
            cnt = 0
            for c in candies:
                if c >= mid:
                    cnt += c//mid
                if cnt >= k:
                    break
            if cnt >= k:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans

