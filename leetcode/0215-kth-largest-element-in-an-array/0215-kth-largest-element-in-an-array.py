class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k
        def partition(nums):            
            if len(nums) <= 1:
                return 
            m = (len(nums)-1)//2
            p = nums[m]
            left = []
            right = []
            mid = []
            
            for n in nums:
                if n < p:
                    left.append(n)
                elif n == p:
                    mid.append(n)
                else:
                    right.append(n)

            return left, mid, right

        def quicksort(nums):
            nonlocal k 
            if len(nums) <= 1:
                return nums[0]
            left, mid, right  = partition(nums)

            # print(k, left,mid, right)

            if k < len(left):
                return quicksort(left)
            elif k < len(left) + len(mid):
                return mid[0]
            else:
                k -= len(left) + len(mid)
                return quicksort(right)
        # print(quicksort(nums))
        return quicksort(nums)
            
