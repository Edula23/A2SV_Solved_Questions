class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        solved = False
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        boxes = [set() for i in range(9)]

        for i in range(9):
            for j in range(9):
                n = board[i][j]
                if n != ".":
                    rows[i].add(int(n))
                    cols[j].add(int(n))

                    boxId = (i // 3) * 3 + j // 3
                    boxes[boxId].add(int(n))
        def backTrack(i, j):
            nonlocal solved
            if i == 9:
                solved = True
                return
            new_i = i + (j+1)//9
            new_j = (j+1) % 9

            if board[i][j] != ".":
                backTrack(new_i, new_j)
            else:
                for n in range(1, 10):
                    boxId = (i // 3) * 3 + j // 3
                    if n not in rows[i] and n not in cols[j] and n not in boxes[boxId]:
                        rows[i].add(n)
                        cols[j].add(n)
                        boxes[boxId].add(n)
                        board[i][j] = str(n)

                        backTrack(new_i, new_j)

                        if not solved:
                            rows[i].remove(n)
                            cols[j].remove(n)
                            boxes[boxId].remove(n)
                            board[i][j] = "."
        backTrack(0, 0)
        return board

         