class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n - 1
        if nums[l] > nums[r]:
            while l < r:
                mid = (l + r) // 2
                
                if nums[mid] == target:
                    return mid
                if nums[mid] > nums[r]:
                    l = mid + 1
                else:
                    r = mid

            if target > nums[n - 1]:
                l, r = 0, l - 1
            else:
                l, r = l, n - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1