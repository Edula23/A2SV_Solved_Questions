class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        nums.sort(reverse=True)
        maxx = res =  0
        for n in requests:
            maxx = max(maxx, n[1])
        prefix = [0] * (len(nums)+1)
        for l, r in requests:
            prefix[l] += 1
            prefix[r+1] -= 1
        for i in range(1, len(prefix)):
            prefix[i] += prefix[i-1]
        prefix.sort(reverse=True)
        for i in range(len(nums)):            
            res += (prefix[i] * nums[i])
        return res % (10**9 + 7)


