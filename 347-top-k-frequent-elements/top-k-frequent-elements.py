import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)

        pq = [(-value, key) for key, value in counter.items()]
        pq = sorted(pq)

        mf = []
        for tp in pq:
            mf.append(tp[-1])
            if len(mf) == k:
                return mf
            

        