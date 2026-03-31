class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        lmax, rmax = [0] * n, [0] * n
        lmax[0], rmax[n - 1] = height[0], height[n - 1]
        
        for i in range (1, n):
            lmax[i] = max(lmax[i - 1], height[i])
            rmax[n - i - 1] = max(rmax[n - i], height[n - i - 1])
        
        res = 0
        for i in range(1, n - 1):
            res += min(lmax[i], rmax[i]) - height[i]
        return res