class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minP = prices[0]
        maxP = 0

        for price in prices:
            minP = min(minP, price)
            maxP = max(maxP, price-minP)
        return maxP