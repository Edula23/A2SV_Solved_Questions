class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        r = len(matrix)
        c = len(matrix[0])
        self.prefix = [[0 for i in range(c+1)] for j in range(r+1)]
        for i in range(r):
            for j in range(c):
                self.prefix[i][j] = matrix[i][j] + self.prefix[i-1][j] + self.prefix[i][j-1] - self.prefix[i-1][j-1]        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        print()
        whole = self.prefix[row2][col2]
        left = self.prefix[row2][col1-1]
        right = self.prefix[row1-1][col2]
        overlap = self.prefix[row1-1][col1-1]
        return whole - left - right + overlap      


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)