class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        charset = set()

        l, r = 0, 0

        for r in range(n):
            while s[r] in charset:
                charset.remove(s[l])
                l += 1
            charset.add(s[r])
            ans = max(ans, len(charset))
        return ans