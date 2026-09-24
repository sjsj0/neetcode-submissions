class Solution:

    ## Recursion --------------------------
    def numDecodings(self, s: str) -> int:
        n=len(s)
        res=0

        # if s[0]=='0':
        #     return res

        def dfs(i):
            nonlocal res
            if i>=n:
                print(i)
                res+=1
                return

            if s[i]=='0':
                return

            dfs(i+1)
            if i<n-1 and int(s[i:i+2])<=26:
                dfs(i+2)

        dfs(0)
        return res


    # ## Recursion --------------------------
    # def numDecodings(self, s: str) -> int:
    #     n=len(s)
    #     res=0

    #     if s[0]=='0':
    #         return res

    #     def dfs(i):
    #         nonlocal res
    #         if i>=n:
    #             print(i)
    #             res+=1
    #             return

    #         if s[i]=='0':
    #             return

    #         dfs(i+1)
    #         if i<n-1 and int(s[i:i+2])<=26:
    #             dfs(i+2)

    #     dfs(0)
    #     return res