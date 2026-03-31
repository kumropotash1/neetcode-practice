class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        visit = set()

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 1 or (r,c) in visit:
                return 0
            if r == rows - 1 and c == cols - 1:
                return 1
            
            visit.add((r,c))
            count = 0
            count += dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)
            visit.remove((r,c))

            return count
        
        return dfs(0, 0)