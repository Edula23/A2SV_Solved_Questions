class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        n = len(nums1)
        nums = [0] * n
        for i in range(n):
            nums[i] = nums1[i] - nums2[i]
        def pairs(l, r, nums, diff):
            if l == r:
                return 0
            m = (l+r)//2
            res = pairs(l, m, nums, diff) + pairs(m+1, r, nums, diff)
            l1, r1, l2, r2 = l, m, m+1, r
            merged = []

            for j in range(l2, r2+1):
                maxx = nums[j] + diff
                pos = bisect_right(nums, maxx, l1, m+1)
                if pos - 1 >= l1:
                    res += (pos- l1)
            
            while l1 <= r1 and l2 <= r2 :
                if nums[l1] <= nums[l2]:
                    merged.append(nums[l1])
                    l1+=1
                else:
                    merged.append(nums[l2])
                    l2+=1
            while l1 <= m:
                merged.append(nums[l1])
                l1 += 1

            while l2 <= r:
                merged.append(nums[l2])
                l2 += 1

            for j in range(l, r+1):
                nums[j] = merged[j-l]
            return res

        return pairs(0, n-1, nums, diff)
