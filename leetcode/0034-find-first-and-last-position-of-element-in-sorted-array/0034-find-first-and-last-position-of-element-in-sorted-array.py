class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = []
        def find_first(nums, res):
            low, high = 0, len(nums) - 1            
            while low <= high:
                mid = (low + high)//2
                if nums[mid] < target:
                    low = mid + 1
                elif nums[mid] >= target:
                    high = mid - 1
            if high + 1 < len(nums) and nums[high + 1] == target:
                res.append(high+1)
            else:
                res.append(-1)

        def find_last(nums, res):
            low, high = 0, len(nums) - 1            
            while low <= high:
                mid = (low + high)//2
                if nums[mid] <= target:
                    low = mid + 1
                elif nums[mid] > target:
                    high = mid - 1
            if low - 1 >= 0 and nums[low - 1] == target:
                res.append(low-1)
            else:
                res.append(-1)

        find_first(nums, res)
        find_last(nums, res)
        return res

            
