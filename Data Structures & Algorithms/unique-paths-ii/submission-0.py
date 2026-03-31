class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] or obstacleGrid[m-1][n-1]:
            return 0

        table = [[0] * (n + 1) for _ in range(m + 1)]
        table[m - 1][n - 1] = 1

        for r in range(m - 1, -1, -1):
            for c in range (n - 1, -1, -1):
                if obstacleGrid[r][c]:
                    table[r][c] = 0
                else:
                    table[r][c] += table[r + 1][c] + table[r][c + 1]

        return table[0][0]