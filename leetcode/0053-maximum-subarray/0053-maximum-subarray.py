class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = float(-inf)
        prefix = [0] * (len(nums))
        minum = summ= 0
        for i in range(len(nums)):
            summ += nums[i]
            prefix[i] +=  summ
        print(prefix)
        for i in range(len(prefix)):
            res = max(res, prefix[i] -minum)
            minum = min(minum, prefix[i])
        return res



        