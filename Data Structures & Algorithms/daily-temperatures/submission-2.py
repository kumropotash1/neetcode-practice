class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        result = [0] * n

        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                prev_temp, j = stack.pop()
                result[j] = i - j
            stack.append((t, i))
        return result