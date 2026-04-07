class Solution:
    def hIndex(self, citations: List[int]) -> int:
        res = float('-inf')
        def binary(n):
            low, high = 0, len(citations)
            while low <= high:
                mid = (low + high)//2
                if mid < len(citations) and citations[mid] >= n:
                    high = mid - 1
                else:
                    low = mid + 1
            return len(citations) - high - 1
        for i in range(0, len(citations)+1):
            amt = binary(i)
            if amt >= i:
                res = max(res, i)
        return res
            
