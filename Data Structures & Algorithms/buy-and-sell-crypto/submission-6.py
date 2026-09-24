class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # DP
        # profit = 0
        # minBuy = prices[0]

        # for sell in prices:
        #     profit = max(profit, sell-minBuy)
        #     minBuy = min(minBuy, sell)

        # return profit

        # Two pointers
        l=0
        r=1
        profit=0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = max(profit, prices[r]-prices[l])
            else:
                l=r
            r += 1

        return profit