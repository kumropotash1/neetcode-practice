class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 1: return 0
        l, r = 0, n - 1
        lmax, rmax = height[l], height[r]
        sum = 0
        while l < r:
            if lmax < rmax:
                l += 1
                if height[l] > lmax:
                    lmax = height[l]
                sum += lmax - height[l]
            else:
                r -= 1
                if height[r] > rmax:
                    rmax = height[r]
                sum += rmax - height[r]
        return sum