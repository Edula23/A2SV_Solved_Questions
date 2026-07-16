class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        rowT, colT, orig = len(grid), len(grid[0]), grid[row][col]
        visited = [[0 for _ in range(colT)] for _ in range(rowT)]
        dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        def dfs(r, c):
            if r < 0 or r >= rowT or c < 0 or c >= colT or visited[r][c] == 1 or grid[r][c] != orig:
                return
            visited[r][c] = 1
            for d in dir:
                newR = r + d[0]
                newC = c + d[1]
                dfs(newR, newC)
        def onborder(r, c):
            if r==0 or r==rowT-1 or c==0 or c==colT-1:
                return True
            l, ri, u, d = visited[r][c-1], visited[r][c+1], visited[r-1][c], visited[r+1][c]
            if not l or not ri or not u or not d:
                return True
            return False
        def colorborder():
            for i in range(rowT):
                for j in range(colT):
                    if visited[i][j] == 1 and onborder(i, j):
                        grid[i][j] = color
        dfs(row, col)
        colorborder()
        return grid
