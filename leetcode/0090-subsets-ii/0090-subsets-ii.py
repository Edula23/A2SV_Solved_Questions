class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def backTrack(curr, n):
            res.append(curr[:])                      
            for i in range(n, len(nums)):
                if i > n and nums[i] == nums[i-1]:
                    continue
                curr.append(nums[i])
                backTrack(curr, i+1)
                curr.pop()
        backTrack([], 0)
        return res
        