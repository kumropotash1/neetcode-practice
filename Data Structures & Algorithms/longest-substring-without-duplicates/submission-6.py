class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        l, charset, ans = 0, set(), 1
        
        for r in range(len(s)):
            rchar = s[r]
            while rchar in charset:
                lchar = s[l]
                charset.remove(lchar)
                l += 1
            charset.add(rchar)
            ans = max(ans, r - l  +1)
        return ans