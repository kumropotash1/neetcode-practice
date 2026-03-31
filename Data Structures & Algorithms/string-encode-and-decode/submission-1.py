class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []: return ""

        res = ""

        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        if s == "": return []
        
        res = []
        i = 0

        while i < len(s):
            j = i+1
            while s[j] != "#":
                j += 1
            l = 0
            while i < j:
                l = 10 * l + ord(s[i]) - ord('0')
                i += 1
            word = s[j + 1 : j + l + 1]
            res.append(word)
            i = j + l + 1
        
        return res
            