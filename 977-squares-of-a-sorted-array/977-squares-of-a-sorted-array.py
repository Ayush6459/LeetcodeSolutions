class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        '''
        # brute force approach 
        return sorted([i*i for i in nums])'''
        
        # O(N) solution using two pointer approach
        start = 0
        end = len(nums)-1
        result = [None]*len(nums)
        resultIndex = len(nums)-1
        while start<=end:
            if abs(nums[start])>abs(nums[end]):
                result[resultIndex] = nums[start]**2
                resultIndex -= 1
                start += 1
            else:
                result[resultIndex] = nums[end]**2
                resultIndex -= 1
                end -= 1
        return result