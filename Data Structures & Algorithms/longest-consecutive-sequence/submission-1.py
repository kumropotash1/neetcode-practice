class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ns = set(nums)
        ans = 0

        for n in nums:
            length = 1
            if (n - 1) not in nums:
                while (n + length) in nums:
                    length += 1
                ans = max(ans, length)
        
        return ans