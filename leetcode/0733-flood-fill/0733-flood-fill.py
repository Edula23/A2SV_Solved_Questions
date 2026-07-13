class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        orig = image[sr][sc]
        def inbound(row, col):
            return (0 <= row < len(image) and 0 <= col < len(image[0]))
        def dfs(i, j):
            if image[i][j] == color or image[i][j] != orig:
                return
            image[i][j] = color
            for d in dir:
                newR = i + d[0]
                newC = j + d[1]
                if inbound(newR, newC):
                    dfs(newR, newC)
            return
        dfs(sr, sc)
        return image