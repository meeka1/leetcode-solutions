import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            if num not in counter.keys():
                counter[num] = 1
            else:
                counter[num] += 1

        """
        counter = {
            1: 3,
            2: 2,
            3: 1
        }
        """
        
        pq = [(-value, key) for key, value in counter.items()]
        print("pq before:", pq)
        heapq.heapify(pq)
        pq = sorted(pq)

        print("pq after:", pq)
        mf = []
        for tp in pq:
            mf.append(tp[-1])
            if len(mf) == k:
                return mf
            

        