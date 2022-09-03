import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = []
        heapq.heapify(distance)
        
        for i in points:
            d = i[0]**2 + i[1]**2 
            heapq.heappush(distance,[d*-1,i])
            if len(distance)>k:
                heapq.heappop(distance)
            
        
        return [i[1] for i in distance]
        