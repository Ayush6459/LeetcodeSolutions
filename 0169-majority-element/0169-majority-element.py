class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        '''
            approach 1 : Sort the array then count the element and return the element which has most count.
            
            approach 2 : make a map with key as a elements in array and count as a value and then traverse through the map and return the element with max count value. 
        '''
        # approach 3 : Moore voting algo (Best approach)
        
        candidate = -1
        votes = 0
        for i in nums :
            if votes == 0:
                candidate = i
                votes+=1
            else:
                if i == candidate:
                    votes+=1
                else:
                    votes-=1
                
        count = 0
        for i in nums :
            if i == candidate :
                count+=1
        if count >= len(nums)//2:
            return candidate
        else :
            return -1