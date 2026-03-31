class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 1: return 0
        l, r = 0, n - 1
        lmax, rmax = height[l], height[r]
        sum = min(lmax, rmax) * (r - l - 1)
        while l < r:
            if height[l] < height[r]:
                l += 1
                if l == r:
                    return sum
                sum -= min(lmax, height[l])
                if height[l] > lmax:
                    sum += (min(height[l], rmax) - min(lmax, rmax)) * (r - l - 1)
                    lmax = height[l]
            else:
                r -= 1
                if l == r:
                    return sum
                sum -= min(rmax, height[r])
                if height[r] > rmax:
                    sum += (min(lmax, height[r]) - min(lmax, rmax)) * (r - l - 1)
                    rmax = height[r]
        return sum