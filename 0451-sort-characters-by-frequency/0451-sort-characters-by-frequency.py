import heapq
class Solution:
    def frequencySort(self, s: str) -> str:
        freq = collections.Counter(s)
        heap = []
        heapq.heapify(heap)
        for i in freq:
            heapq.heappush(heap,[-freq[i],i])
        x = ''
        while heap:
            y = heapq.heappop(heap)
            x+=y[1]*(-1*y[0])
        return x