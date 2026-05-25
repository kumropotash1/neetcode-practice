class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []

        nums.sort()

        def dfs(i, combination, sum):
            if sum == target:
                ans.append(combination.copy())
                return

            for j in range(i, len(nums)):
                if sum + nums[j] > target:
                    return
                combination.append(nums[j])
                dfs(j, combination, sum + nums[j])
                combination.pop()
        dfs(0, [], 0)
        return ans
