class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        paci, atl = set(), set()
        ans = []
        def dfs(r, c, prev, visited):
            if r < 0 or c < 0 or r >= rows or c >= cols or (r, c) in visited or heights[r][c] < prev:
                return
            visited.add((r, c))
            dfs(r, c+1, heights[r][c], visited)
            dfs(r+1, c, heights[r][c], visited)
            dfs(r, c-1, heights[r][c], visited)
            dfs(r-1, c, heights[r][c], visited)
        for i in range(cols):
            dfs(0, i, heights[0][i], paci)
            dfs(rows-1, i, heights[rows-1][i], atl)
        for i in range(rows):
            dfs(i, 0, heights[i][0], paci)
            dfs(i, cols-1, heights[i][cols-1], atl)
        for i in range(rows):
            for j in range(cols):
                if (i, j) in paci and (i, j) in atl:
                    ans.append([i,j])
        return ans