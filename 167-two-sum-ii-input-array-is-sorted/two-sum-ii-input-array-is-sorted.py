class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        lp, rp = 0, len(numbers) - 1

        while lp <= rp:
            if numbers[lp]+numbers[rp] > target:
                rp -=1
            elif numbers[lp]+numbers[rp] < target:
                lp += 1
            else:
                return [lp+1, rp+1]
