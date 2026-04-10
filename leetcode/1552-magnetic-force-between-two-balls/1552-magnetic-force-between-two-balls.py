class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        
        left = 1
        right = position[-1] - position[0]
        ans = 0
        
        def canPlace(d):
            count = 1
            prev = position[0]
            
            for i in range(1, len(position)):
                if position[i] - prev >= d:
                    count += 1
                    prev = position[i]
                if count >= m:
                    return True
            
            return False
        
        while left <= right:
            mid = (left + right) // 2
            
            if canPlace(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return ans