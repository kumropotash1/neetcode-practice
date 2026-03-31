class Solution:
    def countBits(self, n: int) -> List[int]:
        table = [0] * (n + 1)
        for i in range(1, n + 1):
            table[i] = table[i >> 1] + (i & 1)
        return table