class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = nums1 + nums2
        arr.sort()
        if len(arr) % 2 == 0:
            first = (len(arr)//2) - 1
            sec = first + 1
            return (arr[first] + arr[sec])/2
        else:
            return arr[len(arr)//2]