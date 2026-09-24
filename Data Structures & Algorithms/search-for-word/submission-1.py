class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        down = len(board)
        right = len(board[0])

        visited = [[False for _ in range(right)] for _ in range(down)]
        st = []

        def dfs(s, x,y):
            if x<0 or x>=down or y<0 or y>=right or visited[x][y] or len(s) > len(word):
                return False

            print(f's:{s} --> x:{x}, y:{y}')
            visited[x][y] = True

            s = s + board[x][y]
            st.append(s)
            if s == word:
                return True

            res = (dfs(s, x-1, y) or dfs(s, x, y+1) or dfs(s, x+1, y) or dfs(s, x, y-1))
            visited[x][y] = False
            return res


        for i in range(down):
            for j in range(right):
                if board[i][j] == word[0]:
                    if dfs("", i,j):
                        return True

        print(st)
        return False