import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = dict()
        for i in nums:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i]+=1
        hp  = []
        heapq.heapify(hp)
        for i in freq:
            heapq.heappush(hp,[freq[i],i])
            if len(hp)>k:
                heapq.heappop(hp)
        return [i[1] for i in hp]