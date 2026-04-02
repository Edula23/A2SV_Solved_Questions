# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low, high = 1, n
        prev = False
        while low <= high:
            mid = (low + high)//2
            if not isBadVersion(mid):
                low = mid+1
            else:
                if isBadVersion(mid) and not isBadVersion(mid-1):
                    return mid
                high = mid - 1


