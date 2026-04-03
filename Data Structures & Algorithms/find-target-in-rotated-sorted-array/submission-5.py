class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n - 1
        if nums[l] > nums[r]:
            while l <= r:
                mid = (l + r) // 2
                
                if nums[mid] == target:
                    return mid
                if mid == r or nums[mid] > nums[mid + 1]:
                    pivot = mid
                    break
                if nums[mid] > nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1

            if target >= nums[l]:
                l, r = 0, pivot
            else:
                l, r = pivot + 1, n - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1