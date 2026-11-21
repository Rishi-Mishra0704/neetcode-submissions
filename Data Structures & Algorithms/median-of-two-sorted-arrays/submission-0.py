class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # binary search on the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)
        half = (m + n + 1) // 2      # size of the left half

        left = 0
        right = m

        while left <= right:
            i = (left + right) // 2  # how many taken from nums1
            j = half - i             # rest come from nums2

            # values around the cut, with sentinels at the edges
            if i > 0:
                left1 = nums1[i - 1]
            else:
                left1 = float('-inf')
            if i < m:
                right1 = nums1[i]
            else:
                right1 = float('inf')
            if j > 0:
                left2 = nums2[j - 1]
            else:
                left2 = float('-inf')
            if j < n:
                right2 = nums2[j]
            else:
                right2 = float('inf')

            if left1 <= right2 and left2 <= right1:
                # correct cut
                if (m + n) % 2 == 1:
                    return float(max(left1, left2))
                return (max(left1, left2) + min(right1, right2)) / 2
            elif left1 > right2:
                right = i - 1        # took too many from nums1
            else:
                left = i + 1         # took too few from nums1

        return 0.0