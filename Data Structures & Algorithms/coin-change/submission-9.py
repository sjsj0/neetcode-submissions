class Solution:
    
    # ## Recursion ------------------------------
    # def coinChange(self, coins: List[int], amount: int) -> int:
        
    #     if amount==0:
    #         return 0
    #     res = float('inf')

    #     def dfs(v, level):
    #         nonlocal res
    #         if v==0:
    #             res = min(res, level)
    #             return

    #         if v<0:
    #             return

    #         for c in coins:
    #             if c<=v:
    #                 dfs(v-c, level+1)

    #     dfs(amount, 0)
    #     return res if res!=float('inf') else -1


    # ## Recursion --------------------------
    # def coinChange(self, coins: List[int], amount: int) -> int:

    #     def dfs(amount):
    #         if amount==0:
    #             return 0

    #         res= 1e9
    #         for c in coins:
    #             if amount>=c:
    #                 res = min(res, 1+dfs(amount-c))

    #         return res

    #     minCoins = dfs(amount)
    #     return -1 if minCoins >=1e9 else minCoins


    ## DP (Top-Down) --------------------------
    def coinChange(self, coins: List[int], amount: int) -> int:

        cache ={}

        def dfs(amount):
            if amount==0:
                return 0

            if amount in cache:
                return cache[amount]

            res= 1e9

            for c in coins:
                if amount>=c:
                    res = min(res, 1+dfs(amount-c))
            
            cache[amount] = res
            return res

        minCoins = dfs(amount)
        return -1 if minCoins >=1e9 else minCoins
