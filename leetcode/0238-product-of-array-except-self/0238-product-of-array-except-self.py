class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        curr = 1
        r = 0
        for i in range(1, len(nums)):
            curr *= nums[r]
            res[i] *= curr
            r+=1
        l = len(nums)-1
        curr = 1
        for i in range(-2, -(len(nums)+1), -1):
            curr*= nums[l]
            res[i] *= curr
            l-=1
        return res