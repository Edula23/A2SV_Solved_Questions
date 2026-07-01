class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        total = sum(quantities)
        def check(q):
            stores = 0
            for p in quantities:
                stores += ceil(p/q)
                if stores > n:
                    return stores
            return stores
        
        low, high = 1, max(quantities)
        ans = high
        while low <= high:
            mid = (low + high)//2
            val = check(mid)
            if val <= n:
                high = mid-1
                ans = min(ans, mid)
            else:
                low = mid + 1
        return ans
                
                
            
            
 