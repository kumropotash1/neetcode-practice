class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        memo = {}
        def dp(i: int, w: int, p: int) -> int:
            if w > capacity:
                return -1

            if i == len(weight):
                if w <= capacity:
                    return p
                return -1

            v1 = dp(i + 1, w + weight[i],  p + profit[i])
            v2 = dp(i + 1, w,  p)
            return max(v1, v2)
        
        return dp(0, 0, 0)