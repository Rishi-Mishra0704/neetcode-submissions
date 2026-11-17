class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1]*n
        left_pass = 1
        for i in range(n):
            answer[i] = left_pass
            left_pass *= nums[i]
        right_pass = 1
        for i in range(n-1,-1,-1):
            answer[i] *= right_pass
            right_pass *= nums[i]
        return answer