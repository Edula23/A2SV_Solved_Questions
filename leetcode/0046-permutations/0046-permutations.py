class Solution:
    def permute(self, nums):
        res = []
        path = []
        used = [False] * len(nums)

        def backtrack():
            if len(path) == len(nums):
                res.append(path[:])
                return
            
            for i in range(len(nums)):
                if used[i]:
                    continue
                
                path.append(nums[i])
                used[i] = True
                
                backtrack()
                
                # undo
                path.pop()
                used[i] = False
        
        backtrack()
        return res