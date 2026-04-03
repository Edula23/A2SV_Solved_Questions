class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        houses.sort()
        ans = float('-inf')
        def findClosest(heaters, house):
            minDis = float('inf')
            left, right = 0, len(heaters) - 1
            while left <= right:
                mid = (left + right)//2
                minDis = min(minDis, abs(heaters[mid] - house))
                if heaters[mid] < house:
                    left = mid + 1
                else:
                    right = mid - 1
            return minDis
        for house in houses:
            ans = max(ans, findClosest(heaters, house))
        return ans
        


