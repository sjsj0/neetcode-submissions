class Solution:
    # def exist(self, board: List[List[str]], word: str) -> bool:
    #     down = len(board)
    #     right = len(board[0])

    #     visited = [[False for _ in range(right)] for _ in range(down)] ## very imp
    #     st = []

    #     def dfs(s, x,y):
    #         if x<0 or x>=down or y<0 or y>=right or visited[x][y] or len(s) > len(word):
    #             return False

    #         visited[x][y] = True
    #         s = s + board[x][y]
    #         st.append(s)
    #         if s == word:
    #             return True

    #         res = (dfs(s, x-1, y) or dfs(s, x, y+1) or dfs(s, x+1, y) or dfs(s, x, y-1))
    #         visited[x][y] = False
    #         return res


    #     for i in range(down):
    #         for j in range(right):
    #             if board[i][j] == word[0]:
    #                 if dfs("", i,j):
    #                     return True

    #     print(st)
    #     return False

    # ## Backtracking optimized ---------------------------------------
    # ## removed visited and used a # char to identify if I visited the cell earlier or not
    # ## and putting the value back to that cell when leaving
    # def exist(self, board: List[List[str]], word: str) -> bool:
    #     down = len(board)
    #     right = len(board[0])

    #     # visited = [[False for _ in range(right)] for _ in range(down)] ## very imp
    #     st = []

    #     def dfs(s, x,y):
    #         if x<0 or x>=down or y<0 or y>=right or board[x][y] == "#" or len(s) > len(word):
    #             return False

    #         # visited[x][y] = True
    #         s = s + board[x][y]
    #         board[x][y] = "#"
    #         st.append(s)
    #         if s == word:
    #             return True

    #         res = (dfs(s, x-1, y) or dfs(s, x, y+1) or dfs(s, x+1, y) or dfs(s, x, y-1))
    #         board[x][y] = s[-1]
    #         # visited[x][y] = False
    #         return res


    #     for i in range(down):
    #         for j in range(right):
    #             if board[i][j] == word[0]:
    #                 if dfs("", i,j):
    #                     return True

    #     print(st)
    #     return False


    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c, i):
            if i == len(word):
                return True
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or word[i] != board[r][c] or board[r][c] == '#'):
                return False

            board[r][c] = '#'
            res = (dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1) or dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1))
            board[r][c] = word[i]
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False