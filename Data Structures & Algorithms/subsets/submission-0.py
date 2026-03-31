class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        subset = []
        n = len(nums)
        def ss(i: int):
            if i >= n:
                ans.append(subset.copy())
                return
            subset.append(nums[i])
            ss(i + 1)
            subset.pop()
            ss(i + 1)
        ss(0)
        return ans