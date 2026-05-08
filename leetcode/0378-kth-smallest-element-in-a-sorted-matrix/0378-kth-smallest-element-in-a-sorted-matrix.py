class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        mat = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                mat.append(matrix[i][j])
        heapify(mat)
        for i in range(len(mat)):
            
            if i + 1 == k:
                return mat[0]
            res = heappop(mat)
