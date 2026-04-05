class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        char_addr_map = {}

        l = 0

        for r in range(n):
            if s[r] in char_addr_map:
                l = max(char_addr_map[s[r]] + 1, l)
            char_addr_map[s[r]] = r
            ans = max(ans, r - l + 1)
        return ans