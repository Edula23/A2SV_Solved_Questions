class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        nums = []
        for i in range(len(nums1)):
            nums.append(nums1[i]-nums2[i])

        res = []
        cnt = 0
        for i in range(len(nums)):
            pos = bisect_left(res, nums[i]+diff+1)
            cnt += pos
            bisect.insort(res, nums[i])

        return cnt