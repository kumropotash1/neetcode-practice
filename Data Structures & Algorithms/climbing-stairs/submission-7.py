class Solution:
    def climbStairs(self, n: int) -> int:
        c0, c1 = 0, 1
        for i in range(n):
            c0, c1 = c1, c0 + c1
        return c1