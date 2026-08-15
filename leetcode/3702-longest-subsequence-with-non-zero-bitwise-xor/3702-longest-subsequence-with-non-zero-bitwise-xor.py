class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        N = len(nums)
        xor = 0
        nonzero = False
        for n in nums:
            xor ^= n
            if n != 0:
                nonzero = True
        if xor != 0:
            return N
        if nonzero:
            return N-1
        return 0
            
            