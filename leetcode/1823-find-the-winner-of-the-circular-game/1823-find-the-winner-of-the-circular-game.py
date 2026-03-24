from collections import defaultdict
class Solution:
    def findTheWinner(self, n: int, k: int) -> int: 
        deleted = []
        c = 1 + k - 1
        for i in range(1, n+1):
            deleted.append(i)
        def helper(deleted, c):
            if len(deleted) == 1:
                return deleted[0]
            while c >= len(deleted):
                c = c - len(deleted)
            deleted.pop(c)
            return helper(deleted, c+k-1)
        res = helper(deleted, k-1)
        return res 
