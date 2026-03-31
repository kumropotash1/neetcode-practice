class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        memo = {}
        n = len(profit)
        def dp(i, c):
            if i >= n:
                return 0
            if (i, c) in memo:
                return memo[(i, c)]
            
            p, w = profit[i], weight[i]

            if w <= c:
                memo[(i, c)] = max(dp(i + 1, c), p + dp(i + 1, c - w))
            else:
                memo[(i, c)] = dp(i + 1, c)
            return memo[(i, c)]
        return dp(0, capacity)