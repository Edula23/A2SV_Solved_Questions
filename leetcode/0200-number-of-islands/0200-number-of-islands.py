class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dir = [(0,1), (0, -1), (1, 0), (-1, 0)]
        cnt = 0
        def notinbound(grid, row, col):
            if len(grid) <= row or len(grid[0]) <= col or col < 0 or row < 0:
                return True
        def dfs(grid, row, col):
            if notinbound(grid, row, col) or grid[row][col] == '0':
                return
            newRow, newCol = 0, 0
            grid[row][col] = '0'
            for d in dir:
                newRow = row + d[0]
                newCol = col + d[1]

                if not notinbound(grid, newRow, newCol):
                    dfs(grid, newRow, newCol)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    cnt += 1
                dfs(grid, i, j)
        return cnt
            
