class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        memo = {}
        n = len(profit)

        def dp(i, c):
            if i >= n:
                return 0
            if (i, c) in memo:
                return memo[(i, c)]
            w = weight[i]
            p = profit[i]
            
            if c < weight[i]:
                memo[(i, c)] = dp(i + 1, c)
            else:
                memo[(i, c)] = max(dp(i + 1, c), profit[i] + dp(i + 1, c - weight[i]))
            return memo[(i, c)]
        return dp(0, capacity)
                