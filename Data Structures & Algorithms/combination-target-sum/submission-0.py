class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        sum = 0
        combination = []

        def dfs(i):
            nonlocal sum
            if sum == target:
                ans.append(combination.copy())
                return
            if sum > target:
                return
            if i >= len(nums):
                return
            
            sum += nums[i]
            combination.append(nums[i])
            dfs(i)

            sum -= nums[i]
            combination.pop()
            dfs(i + 1)
        
        dfs(0)
        return ans
