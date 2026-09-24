class Solution:
    # def solve(self, board: List[List[str]]) -> None:
    #     down = len(board)
    #     right = len(board[0])

    #     def convert(r,c):
    #         if r<0 or r>=down or c<0 or c>=right or board[r][c]!="O":
    #             return

    #         board[r][c] = "T"
    #         convert(r+1,c)
    #         convert(r-1,c)
    #         convert(r,c+1)
    #         convert(r,c-1)

    #     for r in range(down):
    #         if board[r][0] == "O":
    #             convert(r,0)
    #         if board[r][right-1] == "O":
    #             convert(r,right-1)


    #     for c in range(right):
    #         if board[0][c] == "O":
    #             convert(0,c)
    #         if board[down-1][c] == "O":
    #             convert(down-1,c)

    #     for r in range(down):
    #         for c in range(right):
    #             if board[r][c] == "O":
    #                 board[r][c] = "X"
    #             if board[r][c] == "T":
    #                 board[r][c] = "O"

    def solve(self, board: List[List[str]]) -> None:
        down = len(board)
        right = len(board[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        print(down, right)

        def convert():
            queue = deque()

            for r in range(down):
                for c in range(right):
                    if r==0 or r==down-1 or c==0 or c==right-1 and board[r][c] == "O":
                        queue.append((r,c))
            
            while queue:
                r,c = queue.popleft()
                print(r,c)
                if board[r][c] == "O":
                    board[r][c] = "T"
                    for dr,dc in directions:
                        nr = r+dr
                        nc = c+dc
                        if nr>=0 and nr<down and nc>=0 and nc<right:
                            queue.append((nr,nc))

        convert()

        for r in range(down):
            for c in range(right):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "T":
                    board[r][c] = "O"


