class Solution:
    def _normalize_char(self, c: str):
        ord_c = ord(c)
        if ord_c >= self.ord_A and ord_c <= self.ord_Z:
            return ord_c - self.diff
        if (ord_c >= self.ord_a and ord_c <= self.ord_z) or (ord_c >= self.ord_zero and ord_c <= self.ord_nine):
            return ord_c
        return -1
            
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        self.ord_A = ord('A')
        self.ord_Z = ord('Z')
        self.ord_a = ord('a')
        self.ord_z = ord('z')
        self.ord_zero = ord('0')
        self.ord_nine = ord('9')
        self.diff = ord('A') - ord('a')

        while l < r:
            nc_l = self._normalize_char(s[l])
            if nc_l == -1:
                l += 1
                continue
            nc_r = self._normalize_char(s[r])
            if nc_r == -1:
                r -= 1
                continue
            if nc_l != nc_r: return False
            l, r = l + 1, r - 1
        return True