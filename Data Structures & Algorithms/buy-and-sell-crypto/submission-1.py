class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prev_min = prices[0]
        profit = 0
        for price in prices:
            profit = max(profit, price - prev_min)
            prev_min = min(price, prev_min)
        return profit