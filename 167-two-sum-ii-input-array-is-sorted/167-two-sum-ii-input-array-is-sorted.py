class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        left = 0 
        right = len(numbers)-1
        while left<right:
            
            if numbers[left]+numbers[right]==target:
                return [left+1, right+1]
            mid = (left+right)//2
            if numbers[left]+numbers[right]>target:
                right -=1
            
            else:left +=1
        '''
        # solution using two pointer
        i,j = 0,len(nums)-1
        while i<j:
            s = nums[i]+nums[j]
            if s == target:
                return [i+1,j+1]
            elif s<target:
                i+=1
            elif s>target:
                j-=1
        