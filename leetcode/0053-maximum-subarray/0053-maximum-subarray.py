class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = float(-inf)
        prefix = minPre = 0 
        for n in nums:
            prefix+=n
            res = max(res, prefix-minPre)           
            minPre = min(prefix, minPre)                
            
        return res



        