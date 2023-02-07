import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = collections.Counter(nums)
        heap = []
        heapq.heapify(heap)
        for i in freq:
            heapq.heappush(heap,[freq[i],i])
            if len(heap)>k:
                heapq.heappop(heap)
                
        return [y for x,y in heap]
        