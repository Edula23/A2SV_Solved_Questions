class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res = set()
        ans = []
        for i in range(len(nums)):
            if nums[i] in res:
                ans.append(nums[i])
            else:
                res.add(nums[i])
        for i in range(1, len(nums) + 1):
            if i not in res:
                ans.append(i)
                break
        return ans