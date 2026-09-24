class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        subRes = []

        def toPlace(queenNo, pos):
            for j in range(queenNo):
                if (subRes[j] == pos) or (abs(j-queenNo) == abs(subRes[j]-pos)):
                    return False
            return True

        def makeQ(i, total):
            string = "." * total
            string = string[:i] + "Q" + string[i+1:]
            return string

        def dfs(queenNo):
            for pos in range(n):
                if toPlace(queenNo, pos):
                    subRes.append(pos)        ## queen to alloted to this posiiton (subres[0] - tells about Q0)
                    if queenNo >= n-1:
                        res.append(subRes.copy())
                    else:
                        dfs(queenNo+1)
                    subRes.pop()

        dfs(0)      ## starting with 1st queen i.e., Q0
        print(res)
        ans = []
        for arr in res:
            subAns = []
            for element in arr:
                subAns.append(makeQ(element,n))
            ans.append(subAns.copy())

        return ans


