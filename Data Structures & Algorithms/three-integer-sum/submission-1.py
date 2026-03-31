class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort() # in-place

        res = []
        for i in range(n):
            j, k = i + 1, n - 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            while j < k:
                if j > i + 1 and nums[j] == nums[j - 1]:
                    j += 1
                    continue
                if k < n - 1 and nums[k] == nums[k + 1]:
                    k -= 1
                    continue
                s = nums[i] + nums[j] + nums[k]
                if s == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                elif s > 0:
                    k -= 1
                else:
                    j += 1
        return res