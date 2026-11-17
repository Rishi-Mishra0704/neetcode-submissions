class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        # Step 1: find k, the index of the smallest element (the rotation point)
        lo, hi = 0, n - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > nums[hi]:     # the smallest is to the right of mid
                lo = mid + 1
            else:                        # the smallest is at mid or to its left
                hi = mid
        k = lo

        # Step 2: normal binary search over a "virtual" sorted array
        # virtual index i maps to the real index (i + k) % n
        lo, hi = 0, n - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            real = (mid + k) % n
            if nums[real] == target:
                return real
            elif nums[real] < target:
                lo = mid + 1
            else:
                hi = mid - 1

        return -1