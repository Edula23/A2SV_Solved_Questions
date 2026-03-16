class Solution:
    def nextGreaterElement(self, nums1, nums2):
        n2 = len(nums2)
        ans = [-1] * n2   
        stack = []

        for i in range(n2 - 1, -1, -1):  
            while stack and nums2[i] > stack[-1]:
                stack.pop()
            if stack:
                ans[i] = stack[-1]
            stack.append(nums2[i])

        res = []
        for num in nums1:
            for j in range(n2):
                if nums2[j] == num:
                    res.append(ans[j])
                    break

        return res