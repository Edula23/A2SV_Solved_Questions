class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        count[0] = 1
        summ = ans = 0
        for i in range(len(nums)):
            summ += nums[i]
            if summ % k in count:  
                ans += count[summ % k]
            count[summ % k] += 1
        return ans