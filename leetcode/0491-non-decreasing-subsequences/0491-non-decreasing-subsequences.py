class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backTrack(arr, curr):

            if len(arr) >= 2:
                res.append(arr[:])            

            used = set()
            for i in range(curr, len(nums)):

                if nums[i] in used:
                    continue
                
                if not arr or nums[i] >= arr[-1] :
                    used.add(nums[i])
                    arr.append(nums[i])                    
                    backTrack(arr, i+1)
                    arr.pop()
                
        backTrack([], 0)
        return res

        
