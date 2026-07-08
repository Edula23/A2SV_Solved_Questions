class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = total = 0
        for i in range(len(nums)):
            res += nums[i]
            total += i
        total += len(nums)
        return total - res


 