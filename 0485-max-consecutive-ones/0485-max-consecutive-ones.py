class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        i= 0
        j = 0
        while i<len(nums) and j<len(nums):
            if nums[j] == 0:
                i= j+1
                j+=1
            else:  
                res = max(res,j-i+1)
                j+=1
        return res