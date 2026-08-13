class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        total = 0
        for i in range(k):
            total += nums[i]
        maxSum = total
        for i in range(len(nums)-k):
            total -= nums[i]
            total += nums[i+k]
            maxSum = max(maxSum, total)
        return maxSum / k
