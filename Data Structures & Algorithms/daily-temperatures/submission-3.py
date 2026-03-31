class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n

        for i in range(n - 2, -1, -1):
            j = i + 1
            while j < n:
                if temperatures[i] < temperatures[j]:
                    result[i] = j - i
                    break
                elif result[j] == 0:
                    break
                else:
                    j += result[j]
        return result