class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        t0, t1 = 0, nums[0]
        for i in range(1, n):
            t0, t1 = t1, max(nums[i] + t0, t1)
        return t1