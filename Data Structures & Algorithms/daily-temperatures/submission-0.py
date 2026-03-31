class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack, n = [], len(temperatures)
        result = [0] * n

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                prev, j = stack.pop()
                result[j] = i - j
            stack.append((t, i))
        return result