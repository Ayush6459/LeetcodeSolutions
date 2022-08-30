import heapq
class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums = [-int(i) for i in nums]
        heapq.heapify(nums)
        i = 0
        while i<k-1:
            heapq.heappop(nums) 
            i+=1
        return str(-nums[0])