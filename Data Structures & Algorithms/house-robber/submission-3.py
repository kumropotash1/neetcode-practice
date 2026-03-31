class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = [-1] * len(nums)
        
        def helper(i):
            if i >= len(nums):
                return 0
            if cache[i] != -1:
                return cache[i]
            cache[i] = max(helper(i + 1), nums[i] + helper(i + 2))
            return cache[i]

        return helper(0)