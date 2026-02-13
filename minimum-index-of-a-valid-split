from collections import Counter, defaultdict
class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        count = Counter(nums)
        count1 = defaultdict(int)
        dom = 0
        val = 0
        for k, v in count.items():
            if v > val:
                dom = k
                val = v
        split1 = 0
        split2 = val
        for i in range(len(nums)):
            if nums[i]==dom:
                split1 += 1
                split2 -= 1
                if split1 > (i+1)/2 and split2 > (len(nums) - (i+1))/2:
                    return i
        return -1

            
            
