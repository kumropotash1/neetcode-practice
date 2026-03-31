class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        memo = {}
        def dp(i: int, w: int, p: int) -> int:
            if w > capacity:
                memo[(i, w)] = -1
                return memo[(i, w)]

            if i == len(weight):
                memo[(i, w)] = p
                return memo[(i, w)]

            memo[(i + 1, w + weight[i])] = dp(i + 1, w + weight[i],  p + profit[i])
            memo[(i + 1, w)] = dp(i + 1, w,  p)
            return max(memo[(i + 1, w + weight[i])], memo[(i + 1, w)])
        
        return dp(0, 0, 0)