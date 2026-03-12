class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        minum = nums[0]
        for n in nums:
            while stack and n > stack[-1][0]:
                stack.pop()
            if stack and n < stack[-1][0] and n > stack[-1][1]:
                return True
            
            minum = min(minum, n)
            stack.append([n, minum])
            
            
        return False