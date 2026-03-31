class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        n = len(profit)
        memo = {}
        def dp(i, cap):
            if i >= n: return 0
            if (i, cap) in memo:
                return memo[(i, cap)]
            w = weight[i]
            p = profit[i]

            if w <= cap:
                memo[(i, cap)] = max(p + dp(i + 1, cap - w), dp(i + 1, cap))
            else:
                memo[(i, cap)] = dp(i + 1, cap)
            return memo[(i, cap)]
    
        return dp(0, capacity)