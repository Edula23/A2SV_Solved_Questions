class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        left = 0
        maxLen = 0
        for i in range(len(nums)):
            while count[nums[i]] == k:
                count[nums[left]] -= 1
                left+=1
            count[nums[i]] += 1
            maxLen = max(maxLen, i-left+1)
        return maxLen