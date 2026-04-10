class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, right, mid = 0, len(matrix), 0
        while left <= right and (left + right)//2 < len(matrix):
            mid = (left + right)//2
            print(mid)
            if matrix[mid][0] > target:
                right = mid - 1
            elif matrix[mid][len(matrix[0])-1] < target:
                left = mid + 1
            else:
                l , r = 0, len(matrix[0])-1
                while l <= r:
                    m = (l + r)//2
                    if matrix[mid][m] > target:
                        r = m-1
                    elif matrix[mid][m] < target:
                        l = m + 1
                    elif matrix[mid][m] == target:
                        break
                if matrix[mid][m] == target:
                    return True
                else:
                    return False
        return False