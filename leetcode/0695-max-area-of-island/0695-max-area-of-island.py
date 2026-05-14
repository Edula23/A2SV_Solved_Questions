class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        par = defaultdict()
        size = defaultdict()
        ans = 0
        inbound = lambda r,c: 0 <= r < len(grid) and 0 <= c < len(grid[0])
        dirc = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    par[(i,j)] = (i, j)
                    size[(i,j)] = 1
        def find(x):
            nonlocal par
            if x == par[x]:
                return x
            par[x] = find(par[x])
            return par[x]

        def union(x, y):
            nonlocal par, size
            rx = find(x)
            ry = find(y)
            if rx != ry:
                if size[rx] > size[ry]:
                    par[ry] = rx
                    size[rx] += size[ry]
                    # print(size[rx])
                    return size[rx]
                else:
                    par[rx] = ry
                    size[ry] += size[rx]
                    # print(size[ry])
                    return size[ry] 
            return 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    if ans == 0:
                        ans = 1
                    for x, y in dirc:
                        ni = i + x
                        nj = j + y
                        if inbound(ni, nj) and grid[ni][nj] == 1 :
                            # print(size)
                            ans = max(ans, union((i,j), (ni, nj)))
        return ans

