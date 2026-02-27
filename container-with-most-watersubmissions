class Solution:
    def maxArea(self, height: List[int]) -> int:
        right = len(height) - 1
        left = 0  
        maxArea = 0  
        while left < right:
            width = right - left
            minHeight = min(height[right], height[left])
            area = minHeight * width
            maxArea = max(maxArea, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxArea


            
