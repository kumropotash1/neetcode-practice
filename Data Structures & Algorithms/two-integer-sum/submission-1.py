class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_map = {}

        n = len(nums)

        for i in range(n):
            if target - nums[i] in diff_map: continue
            diff_map[target - nums[i]] = i
        
        for j in range(n-1, -1, -1):
            if nums[j] in diff_map:
                return [diff_map[nums[j]], j]