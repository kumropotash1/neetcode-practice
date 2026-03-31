class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        diff = {}
        for i in range(len(s)):
            cs, ct = s[i], t[i]
            diff[cs] = diff.get(cs, 0) + 1
            diff[ct] = diff.get(ct, 0) - 1

        for v in diff.values():
            if v: return False
        
        return True