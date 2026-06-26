class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        def dac(l, r):
            if l == r:
                return nums[l]
            m = int(l + (r-l)/2)
            lm = dac(l, m)
            rm = dac(m+1, r)
            if lm == rm:
                return lm
            return lm if nums.count(lm) > nums.count(rm) else rm
        return dac(0, len(nums)-1)