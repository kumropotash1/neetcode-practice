class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        table = [0] * (n + 1)
        table[1] = nums[0]
        for i in range(2, n + 1):
            table[i] = max(
                table[i - 1],
                nums[i - 1] + table[i - 2]
            )
        return table[n]