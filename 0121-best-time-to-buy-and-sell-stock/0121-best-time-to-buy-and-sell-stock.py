class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = prices[0]
        maxProfit = 0

        for price in prices:
            if price < mini:
                mini = price
            else:
                maxProfit = max(maxProfit, price - mini)

        return maxProfit
