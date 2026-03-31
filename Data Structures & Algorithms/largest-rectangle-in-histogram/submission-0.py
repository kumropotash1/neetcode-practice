class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        ans = heights[0]

        for i in range(n):
            cur_min = heights[i]
            for j in range(i, n):
                cur_min = min(cur_min, heights[j])
                ans = max(ans, (j - i + 1) * cur_min)
        return ans