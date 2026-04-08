class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(nums):
            if len(nums) > 1:
                left = nums[:len(nums)//2]
                right = nums[len(nums)//2:]
                mergeSort(left)
                mergeSort(right)
                l = r = k = 0
                while l < len(left) and r < len(right):
                    if left[l] < right[r]:
                        nums[k] = left[l]
                        l+= 1
                    else:
                        nums[k] = right[r]
                        r+=1
                    k+=1
                while l < len(left):
                    nums[k] = left[l]
                    l+=1
                    k+=1
                while r < len(right):
                    nums[k] = right[r]
                    r+=1
                    k+=1
        mergeSort(nums)
        return nums

