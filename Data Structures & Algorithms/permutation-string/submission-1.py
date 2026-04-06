class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        
        diff = [0] * 26
        matches = 26

        for i in range(len(s1)):
            ord_c_s1 = ord(s1[i]) - ord('a')
            diff[ord_c_s1] += 1
            if diff[ord_c_s1] == 0:
                matches += 1
            if diff[ord_c_s1] == 1:
                matches -= 1

            ord_c_s2 = ord(s2[i]) - ord('a')
            diff[ord_c_s2] -= 1
            if diff[ord_c_s2] == 0:
                matches += 1
            if diff[ord_c_s2] == -1:
                matches -= 1

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            ord_c_r = ord(s2[r]) - ord('a')
            ord_c_l = ord(s2[l]) - ord('a')
            
            diff[ord_c_r] -= 1
            if diff[ord_c_r] == 0:
                matches += 1
            if diff[ord_c_r] == -1:
                matches -= 1
            
            diff[ord_c_l] += 1
            if diff[ord_c_l] == 0:
                matches += 1
            if diff[ord_c_l] == 1:
                matches -= 1
            
            l += 1

        return matches == 26