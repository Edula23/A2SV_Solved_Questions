class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        res = [0] * len(matrix)
        for i in range(len(matrix)):
            cnt = 0
            for j in range(len(matrix[i])):
                if matrix[i][j] == 1:
                    cnt+=1
            res[i] += cnt
        return res

        