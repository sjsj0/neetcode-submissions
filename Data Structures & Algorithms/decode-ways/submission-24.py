class Solution:

    # ## Recursion --------------------------
    # def numDecodings(self, s: str) -> int:
    #     n=len(s)
    #     res=0

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


    # ## Recursion --------------------------
    # def numDecodings(self, s: str) -> int:
    #     n=len(s)
    #     res=0
    #     cache = {}

    #     def dfs(i):
    #         nonlocal res
    #         if i>=n:
    #             print(i)
    #             res+=1
    #             return 1

    #         if s[i]=='0':
    #             return

    #         if (i+1) in cache:
    #             res += cache[i+1]
    #         else:
    #             cache[i+1] = dfs(i+1)
    #             res += cache[i+1]
            
            
    #         if i<n-1 and int(s[i:i+2])<=26 and (i+2) in cache:
    #             res += cache[i+2]
    #         elif i<n-1 and int(s[i:i+2])<=26:
    #             cache[i+2] = dfs(i+2)
    #             res += cache[i+2]

    #         return res


    #     return dfs(0)

    def numDecodings(self, s: str) -> int:
        n = len(s)
        memo = {}

        def dfs(i):
            # Base case: reached end = 1 valid decoding
            if i == n:
                return 1

            # If leading zero → invalid path
            if s[i] == '0':
                return 0

            # If already computed, return stored value
            if i in memo:
                return memo[i]

            # Take single digit
            ways = dfs(i + 1)

            # Take two digits if valid (10–26)
            if i + 1 < n and 10 <= int(s[i:i+2]) <= 26:
                ways += dfs(i + 2)

            memo[i] = ways
            return ways

        return dfs(0)
