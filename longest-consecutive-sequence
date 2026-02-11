class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n_set = set(nums)
        n_list = list(n_set)
        n_list.sort()
        i = 0
        j = i + 1
        ranges = 1
        while i < len(n_list)-1 and j < len(n_list):            
            if n_list[j] == n_list[j-1]+1 :
                ranges = max(ranges, j - i + 1)
                j += 1                
            else:               
                ranges = max(ranges, j - i) 
                print(ranges)
                i = j
                j = i + 1
        if nums:
            return ranges
        else:
            return 0

            
            
