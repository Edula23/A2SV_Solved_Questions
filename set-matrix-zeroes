class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        indices = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    indices.add((i,j))
        for a, b in indices:
            for k in range(len(matrix[0])):
                matrix[a][k] = 0
            for j in range(len(matrix)):
                matrix[j][b] = 0
        print(matrix)
        

