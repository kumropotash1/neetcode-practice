class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [-1] * (n+1)
        # if n == 1: return 1
        # if n == 2: return 2
        def dfs(i):
            if cache[i] != -1: return cache[i]

            if i == 1:
                cache[i] = 1
            elif i == 2:
                cache[i] = 2
            else:
                cache[i] = dfs(i-1) + dfs(i-2)
            return cache[i]
        
        return dfs(n)

        # return self.climbStairs(n-1) + self.climbStairs(n-2)