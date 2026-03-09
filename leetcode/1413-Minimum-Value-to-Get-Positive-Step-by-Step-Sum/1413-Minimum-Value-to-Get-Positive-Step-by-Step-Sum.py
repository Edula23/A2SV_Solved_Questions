class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix = [0] * len(nums)
        summ = ans = 0
        for i in range(len(nums)):
            summ+=nums[i]
            prefix[i] = summ
        minum = min(prefix)
        if minum < 0:
            ans = -(minum) + 1
        else:
            ans = 1
        return ans