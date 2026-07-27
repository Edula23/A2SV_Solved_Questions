class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        fir = nums[0]
        prev = nums[1]
        for i in range(1, len(nums)):
            val = nums[i]
            if val >= fir:
                prev = fir
                fir = val
            elif val >= prev:
                prev = val
        return (fir-1) * (prev-1)