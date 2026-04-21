class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        dir = [(0,1), (0, -1), (1, 0), (-1, 0)]
        peri = 0
        initial = True
        def notinbound(row, col):
            if len(grid) <= row or len(grid[0]) <= col or row < 0 or col < 0:
                return True
        def dfs(grid, row, col):
            nonlocal peri, initial
            if notinbound(row, col) or grid[row][col] == 0:
                peri += 1
                return
            if grid[row][col] == -1:
                return
            grid[row][col] = -1
            
            for d in dir:
                newR = row + d[0]
                newC = col + d[1]
                dfs(grid, newR, newC)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    dfs(grid, i, j)
                    return peri
        return peri
