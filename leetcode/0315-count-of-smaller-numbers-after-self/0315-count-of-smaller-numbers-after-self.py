from sortedcontainers import SortedList
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        sortedlist = SortedList([])
        res = []
        for i in range(-1, -(len(nums)+1), -1):
            idx = sortedlist.bisect_left(nums[i])
            res.append(idx)
            sortedlist.add(nums[i])
        res.reverse()
        return res
