class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix = [0] * (len(nums) + 1)
        summ = 0
        mp = defaultdict(int)
        mp[0] = 1
        res = 0
        for i in range(len(nums)):
            summ+=nums[i]
            if summ - goal in mp:
                res += mp[summ - goal]
            mp[summ] += 1
        return res


        