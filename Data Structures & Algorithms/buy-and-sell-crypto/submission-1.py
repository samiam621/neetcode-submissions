class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #ex. [5,1,5,6,7,1,10], len = 7
        maxProf= 0
        l,r = 0,1

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r]-prices[l]
                maxProf = max(maxProf,profit)
            else:
                l = r
            r += 1
        return maxProf