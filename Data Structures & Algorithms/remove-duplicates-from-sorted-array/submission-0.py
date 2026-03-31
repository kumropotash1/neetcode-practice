class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        
        count = 1
        for i in range(1, n):
            if nums[count - 1] == nums[i]:
                continue
            if i >= count:
                nums[count] = nums[i]
                count += 1
        return count