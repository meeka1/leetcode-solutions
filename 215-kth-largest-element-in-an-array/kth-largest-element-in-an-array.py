import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-num for num in nums]
        heapq.heapify(nums)

        maxes = []
        for i in range(k):
            popped = heapq.heappop(nums)
            maxes.append(popped)

        return -popped