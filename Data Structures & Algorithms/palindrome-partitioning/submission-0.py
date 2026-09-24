class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        subRes = []

        def dfs(i):
            if i >= len(s):
                res.append(subRes.copy())
                return

            for j in range(i, len(s)):
                print(subRes)
                if s[i:j+1] == s[i:j+1][::-1]:
                    subRes.append(s[i:j+1])
                    dfs(j+1)
                    subRes.pop()
        
        dfs(0)
        return res
