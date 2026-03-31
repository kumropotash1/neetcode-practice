class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        n = len(profit)
        dp = [[0] * (capacity + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for w in range (1, capacity + 1):
                if weight[i - 1] <= w:
                    dp[i][w] = max(
                        dp[i - 1][w],
                        profit[i - 1] + dp[i - 1][w - weight[i - 1]]
                    )
                else:
                    dp[i][w] = dp[i - 1][w]
        
        return dp[n][capacity]