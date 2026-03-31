class Solution:
    def climbStairs(self, n: int) -> int:
        def memoized(i, cache):
            if i < 3:
                return i

            if i in cache:
                return cache[i]
            
            cache[i] = memoized(i-1, cache) + memoized(i-2, cache)
            return cache[i]
        return memoized(n, {})