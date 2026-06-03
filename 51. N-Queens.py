from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        board = [['.'] * n for _ in range(n)]

        def dfs(row: int, cols: int, diag1: int, diag2: int):
            if row == n:
                ans.append([''.join(r) for r in board])
                return

            available = ((1 << n) - 1) & ~(cols | diag1 | diag2)

            while available:
                bit = available & -available
                available -= bit

                col = bit.bit_length() - 1

                board[row][col] = 'Q'

                dfs(
                    row + 1,
                    cols | bit,
                    (diag1 | bit) << 1,
                    (diag2 | bit) >> 1
                )

                board[row][col] = '.'

        dfs(0, 0, 0, 0)
        return ans