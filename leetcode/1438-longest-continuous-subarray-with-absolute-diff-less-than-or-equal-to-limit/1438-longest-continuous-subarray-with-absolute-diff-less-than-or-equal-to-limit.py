class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        minum = deque()
        maxum = deque()
        ans = left = 0
        for right in range(len(nums)):
            while minum and nums[right] < minum[-1]:
                minum.pop()
            minum.append(nums[right])
            while maxum and nums[right] > maxum[-1]:
                maxum.pop()
            maxum.append(nums[right])
            
            while maxum[0] - minum[0] > limit:
                if nums[left] == maxum[0]:
                    maxum.popleft()
                if nums[left] == minum[0]:
                    minum.popleft()
                left+=1        
            ans = max(ans, right-left+1)
        return ans
            

            
            