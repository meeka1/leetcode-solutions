class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        output = [1] * n

        pre = 1
        for i in range(n):
            output[i] = pre
            pre *= nums[i]

        post = 1
        for i in range(n-1, -1, -1):
            output[i] *= post
            post *= nums[i]

        return output