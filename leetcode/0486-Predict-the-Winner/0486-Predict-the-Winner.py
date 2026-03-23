class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        
        def helper(l, r):
            if l == r:
                return nums[l]
            
            take_left = nums[l] - helper(l + 1, r)
            take_right = nums[r] - helper(l, r - 1)
            
            return max(take_left, take_right)
        
        return helper(0, len(nums) - 1) >= 0