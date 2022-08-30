import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones = [i*-1 for i in stones]
        heapq.heapify(stones)
        
        while stones:
            x= heapq.heappop(stones)
            if not stones:
                return -x
            y = heapq.heappop(stones)
            
            if x!=y:
                heapq.heappush(stones,(x-y))
        return 0