class Solution:
    def minOperations(self, nums: List[int]) -> int:
        def flip(nums, i):
            if nums[i] == 0:
                nums[i] = 1
            else:
                nums[i] = 0
        count = 0
        for i in range(len(nums)-2):
            if nums[i] == 0:
                flip(nums, i)
                flip(nums, i+1)
                flip(nums, i+2)
                count += 1
        if nums[-1] == 0 or nums[-2] == 0:
            return -1
        return count