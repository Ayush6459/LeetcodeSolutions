import heapq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = {}
        for i in words:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
                
        heap = []
        heapq.heapify(heap)
        for i in freq:
            heapq.heappush(heap,(-1*freq[i],i))
            
        return [y for x,y in heapq.nsmallest(k,heap)]