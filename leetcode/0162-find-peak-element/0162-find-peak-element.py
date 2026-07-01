class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return nums.index(max(nums))
        low, high = 0, len(nums)-1
        while low<=high:
            mid = (low + high)//2
            if mid-1 >=0 and mid+1 < len(nums): 
                if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                    return mid
                if nums[mid] > nums[mid-1]:
                    low = mid+1
                else:
                    high = mid-1
            else:
                if mid-1 < 0 and nums[mid+1] < nums[mid]:
                    return mid
                if mid+1 >= len(nums) and nums[mid-1] < nums[mid]:
                    return mid
                else:
                    if low < high:
                        low = mid+1
                    else:
                        high = mid-1
                    


