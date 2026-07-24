class Solution:
    def canPartition(self, nums: List[int]) -> bool:
       tot = sum(nums)
       if tot % 2 == 1:
        return False
       target = tot//2
       dp = set()
       dp.add(0)
        
       for i in range(len(nums)):
        newDp = set()
        for t in dp:
            if t == target or t + nums[i] == target:
                return True
            newDp.add(t+nums[i])
            newDp.add(t)
            
        dp = newDp
       if target in dp:
        return True
       return False

    
            