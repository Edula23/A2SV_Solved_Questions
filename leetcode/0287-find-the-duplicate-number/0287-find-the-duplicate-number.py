class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        res = set()
        for i in range(len(nums)):
            if nums[i] in res:
                return nums[i]
            res.add(nums[i])