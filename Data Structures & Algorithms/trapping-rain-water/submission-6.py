class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l, r = 0, n - 1
        sum = 0
        lmax, rmax = height[l], height[r]

        while l < r:
            if lmax < rmax:
                l += 1
                lmax = max(height[l], lmax)
                sum += lmax - height[l]
            else:
                r -= 1
                rmax = max(height[r], rmax)
                sum += rmax - height[r]
        return sum