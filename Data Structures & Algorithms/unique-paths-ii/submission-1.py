class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        if obstacleGrid[0][0] or obstacleGrid[m - 1][n - 1]: return 0
        
        prevrow = [0] * n
        prevrow[n - 1] = 1
        
        for r in range(m - 1, -1, -1):
            currow = [0] * n
            currow[n - 1] = prevrow[n - 1] if obstacleGrid[r][n - 1] == 0 else 0
            for c in range(n - 2, -1, -1):
                if obstacleGrid[r][c]:
                    currow[c] = 0
                else:
                    currow[c] += prevrow[c] + currow[c + 1]
            prevrow = currow
        
        return prevrow[0]