class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1): return False

        m, n = len(s1), len(s2)

        diff = [0] * 26
        matches = 26
        for i in range(n):
            c_s2 = ord(s2[i]) - ord('a')
            diff[c_s2] -= 1
            if diff[c_s2] == -1:
                matches -= 1
            if diff[c_s2] == 0:
                matches += 1

            if i < m:
                c_s1 = ord(s1[i]) - ord('a')
                diff[c_s1] += 1
                if diff[c_s1] == 1:
                    matches -= 1
                if diff[c_s1] == 0:
                    matches += 1
            else:
                c_l_s2 = ord(s2[i - m]) - ord('a')
                diff[c_l_s2] += 1
                if diff[c_l_s2] == 0:
                    matches += 1
                if diff[c_l_s2] == 1:
                    matches -= 1
            print(i, diff, matches)
            if i >= (m - 1) and matches == 26:
                return True
        return False
