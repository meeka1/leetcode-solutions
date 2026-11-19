class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        l = 0
        length = 0

        for r in range(len(nums)):
            if nums[l] != nums[r]:
                l = r
            if nums[r] == 1:
                length = max(length, r-l+1)
        return length