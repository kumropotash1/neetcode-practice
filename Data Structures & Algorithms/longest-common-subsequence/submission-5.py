class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) < len(text2):
            text1, text2 = text2, text1

        m, n = len(text1), len(text2)

        table = [0] * (n + 1)

        for i in range(1, m + 1):
            prev = 0
            for j in range(1, n + 1):
                temp = table[j]
                if text1[i - 1] == text2[j - 1]:
                    table[j] = 1 + prev
                else:
                    table[j] = max(
                        table[j],
                        table[j - 1]
                    )
                prev = temp
        
        return table[n]