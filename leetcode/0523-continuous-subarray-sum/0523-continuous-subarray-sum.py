class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remInd = {}
        prefix = [0] * (len(nums)+1)
        summ = 0
        for i in range(len(nums)):
            summ += nums[i]
            prefix[i+1] +=  summ
        for i, val in enumerate(prefix):
            rem = val % k
            if rem in remInd and i - remInd[rem] > 1 :
                return True
            elif rem not in remInd:
                remInd[rem] = i
        return False
