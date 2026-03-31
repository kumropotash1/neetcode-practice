class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        n = len(profit)
        def dp(i, cap):
            if i >= n: return 0
            w = weight[i]
            p = profit[i]

            if w <= cap:
                return max(p + dp(i + 1, cap - w), dp(i + 1, cap))
            return dp(i + 1, cap)
    
        return dp(0, capacity)