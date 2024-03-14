class Solution:
    def totalNQueens(self, n: int) -> int:
        col = set()
        posDiag = set()
        negDiag = set()

        board = [["."] * n for i in range(n)]
        count = 0
        def backtrack(r):
            nonlocal count
            if r == n:
                count += 1
                return 
            for c in range(n):
                if c in col or (r+c) in posDiag or (r-c) in negDiag:
                    continue
                col.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                board[r][c] = "Q"

                backtrack(r+1)
                col.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                board[r][c] = "."
        backtrack(0)
        return count
        