class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        n = len(profit)
        memo = {}
        def dp(i, cap):
            if i >= n:
                return 0

            if (i, cap) in memo:
                return memo[(i, cap)]

            if cap < weight[i]:
                memo[(i, cap)] = dp(i + 1, cap)
            else:
                memo[(i, cap)] = max(
                    dp(i + 1, cap),
                    profit[i] + dp(i + 1, cap - weight[i])
                )
            return memo[(i, cap)]
            
        return dp(0, capacity)