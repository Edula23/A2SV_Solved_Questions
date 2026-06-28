class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        di = {}
        for i in range(len(nums)):
            if nums[i] not in di:
                di[nums[i]] = i
            else:
                if abs(i - di[nums[i]]) <= k:
                    return True
                else:
                    di[nums[i]] = i
        return False
