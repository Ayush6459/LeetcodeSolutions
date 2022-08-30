import heapq
class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        '''
            IDEA :-
                1-> Build a min heap for first k items
                2-> Traverse from (k+1)th element:
                    a-> compare current element with top of the heap if smaller than 
                        top ignore it
                    b-> else remove the top element and insert the current element in 
                        the min heap
                3-> return the top of the heap
        '''
        
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