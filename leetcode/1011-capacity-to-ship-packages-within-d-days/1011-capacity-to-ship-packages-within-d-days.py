class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def checkDays(n):
            curr = i =0
            need = 1
            while i < len(weights):
                if curr + weights[i] > n:
                    curr = 0
                    need += 1
                curr+=weights[i]
                i+=1
            return need
        low, high = max(weights), sum(weights)
        ans = high
        while low <= high:
            mid = (low + high)//2
            if checkDays(mid) <= days:
                high = mid-1
                ans = min(ans, mid)
            else:
                low = mid+1
                
        return ans

