class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        candidates.sort()
        
        def dfs(i, combination, sum):
            if sum == target:
                ans.append(combination.copy())
                return
            
            if sum > target or i == len(candidates):
                return
            
            combination.append(candidates[i])
            dfs(i + 1, combination, sum + candidates[i])
            combination.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, combination, sum)
        
        dfs(0, [], 0)

        return ans