class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        n = len(profit)
        memo = [0] * (capacity + 1)
        for i in range(n):
            for w in range(capacity, weight[i] - 1, -1):
                memo[w] = max(memo[w], profit[i] + memo[w - weight[i]])
        return memo[capacity]
