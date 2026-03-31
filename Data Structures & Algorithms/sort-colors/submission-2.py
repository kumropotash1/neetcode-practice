class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        counts = [0] * 3

        for n in nums:
            counts[n] += 1
        
        ptr = 0

        for color, count in enumerate(counts):
            for _ in range(count):
                nums[ptr] = color
                ptr += 1
        
        return nums