class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:  # [3, 2, 4], 6
        for j in range(0, len(nums)): # range(0, 3) // j=0 // j=1
            curr = nums[j] # curr=3 // curr=2
            for i in range(j+1, len(nums)): # range(2, 1) // i=1 // i=2 // i=
                x = nums[i] + curr # x=nums[1]+3=2+3=5 // x=nums[2]+3=4+3=7
                if x == target:
                    return [i, j]
                
        return 