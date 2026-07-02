class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        ans, n = 0, len(nums)
        for i in range(n):
            cnt = 0
            for j in range(i, n):
                cnt += 1 if nums[j] == target else -1
                if cnt > 0:
                    ans += 1
        return ans
            