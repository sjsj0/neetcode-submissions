class Solution:
    def solve(self, board: List[List[str]]) -> None:
        down = len(board)
        right = len(board[0])

        def convert(r,c):
            if r<0 or r>=down or c<0 or c>=right or board[r][c]!="O":
                return

            board[r][c] = "T"
            convert(r+1,c)
            convert(r-1,c)
            convert(r,c+1)
            convert(r,c-1)

        for r in range(down):
            if board[r][0] == "O":
                convert(r,0)
            if board[r][right-1] == "O":
                convert(r,right-1)


        for c in range(right):
            if board[0][c] == "O":
                convert(0,c)
            if board[down-1][c] == "O":
                convert(down-1,c)

        for r in range(down):
            for c in range(right):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "T":
                    board[r][c] = "O"