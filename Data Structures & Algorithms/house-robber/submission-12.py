class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        t0, t1 = 0, nums[0]

        for i in range(2, n + 1):
            t0, t1 = t1, max(
                t1,
                nums[i - 1] + t0
            )
        
        return t1