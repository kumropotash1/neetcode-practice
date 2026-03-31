class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        n = len(profit)
        memo = [[0] * (capacity + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for w in range (1, capacity + 1):
                if weight[i - 1] <= w:
                    memo[i][w] = max(
                        memo[i - 1][w],
                        profit[i - 1] + memo[i - 1][w - weight[i - 1]]
                    )
                else:
                    memo[i][w] = memo[i - 1][w]
        return memo[i][capacity]
        