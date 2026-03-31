class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        def memoized(i):
            if i < 3:
                return i

            if i in cache:
                return cache[i]
            
            cache[i] = memoized(i-1) + memoized(i-2)
            return cache[i]
        return memoized(n)