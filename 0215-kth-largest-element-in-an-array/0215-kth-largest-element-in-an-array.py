import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        heapq.heapify(heap)
        for ele in nums:
            heapq.heappush(heap,ele)
            if len(heap)>k:
                heapq.heappop(heap)
        
        return heap[0]