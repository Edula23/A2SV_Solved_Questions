class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        arr = [(nums[i], i) for i in range(len(nums))]
        counts = [0] * len(nums)

        def mergeSort(left, right):

            if left >= right:
                return 
            mid = (left + right) // 2
            mergeSort(left, mid)
            mergeSort(mid+1, right)
            
            merged = []
            rightCount = 0
            l, r = left, mid + 1
            while l <= mid and r <= right:
                if arr[l][0] <= arr[r][0]:
                    counts[arr[l][1]] += rightCount
                    merged.append(arr[l])
                    l+=1
                else:
                    rightCount+=1
                    merged.append(arr[r])
                    r+=1
            while l <= mid:
                counts[arr[l][1]] += rightCount
                merged.append(arr[l])
                l+=1
            while r <= right:
                merged.append(arr[r])
                r+=1
            for i in range(len(merged)):
                arr[left+i] = merged[i]
        
        mergeSort(0, len(nums)-1)
        return counts