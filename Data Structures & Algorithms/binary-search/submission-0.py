class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l<=r:
            med = l + (r - l) // 2
            if target < nums[med]:
                r = med - 1
            elif target > nums[med]:
                l = med + 1
            else: return med
        return -1