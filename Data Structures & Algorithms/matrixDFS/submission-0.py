class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c, visit):
            if r < 0 or c < 0 or r == rows or c == cols or (r, c) in visit or grid[r][c] == 1:
                return 0
            if r == rows - 1 and c == cols - 1:
                return 1

            count = 0

            visit.add((r,c))
            count += dfs(r + 1, c, visit)
            count += dfs(r, c + 1, visit)
            count += dfs(r - 1, c, visit)
            count += dfs(r, c - 1, visit)
            
            visit.remove((r,c))
            return count
        
        return dfs(0, 0, set())