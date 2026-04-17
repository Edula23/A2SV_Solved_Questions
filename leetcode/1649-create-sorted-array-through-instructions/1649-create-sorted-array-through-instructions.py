class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        arr = []
        cost = 0
        for i in instructions:
            l = bisect_left(arr, i)
            r = bisect_right(arr, i)

            cost+=min(l, len(arr)-r)
            bisect.insort(arr, i)
        return cost % (10**9 + 7)