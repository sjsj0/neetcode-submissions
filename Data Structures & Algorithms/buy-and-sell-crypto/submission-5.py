class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxPrice = 0
        minBuy = prices[0]

        for sell in prices:
            maxPrice = max(maxPrice, sell-minBuy)
            minBuy = min(minBuy, sell)

        return maxPrice