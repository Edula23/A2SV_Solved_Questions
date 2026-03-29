class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        ndiag = set()
        pdiag = set()
        res = []
        board = [["."] * n for i in range(n)]
        def backTrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
            for col in range(n):
                if col in cols or r + col in pdiag or r-col in ndiag:
                    continue
                cols.add(col)
                pdiag.add(r+col)
                ndiag.add(r-col)
                board[r][col] = "Q"
                backTrack(r+1)
                cols.remove(col)
                pdiag.remove(r+col)
                ndiag.remove(r-col)
                board[r][col] = "."
        backTrack(0)
        return res


                
