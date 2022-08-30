import heapq
class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums = [int(i) for i in nums]
        x = nums[:k]
        
        #print(x)
        heapq.heapify(x)
        #print(x)
        for i in range(k,len(nums)):
            if nums[i]>x[0]:
                heapq.heappop(x)
                heapq.heappush(x,nums[i])
                
        #print(x)
        return str(x[0])