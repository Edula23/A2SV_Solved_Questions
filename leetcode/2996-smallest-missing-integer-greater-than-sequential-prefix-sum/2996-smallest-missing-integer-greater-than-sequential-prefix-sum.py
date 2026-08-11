class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0] + 1
        tot = nums[0]
        last = 0
        for i in range(1, len(nums)):
            if nums[i-1] + 1 == nums[i]:
                tot += nums[i]
            
            else:
               break
        if tot > 50:
            return tot
        sett = set(nums)
        for i in range(tot, 52):
            if i not in sett:
                return i
