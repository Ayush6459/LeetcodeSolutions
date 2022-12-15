class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = []
        for x,y in zip(l,r):
            ans.append(self.isArithmeticSequence(nums[x:y+1]))
        return ans
        
    def isArithmeticSequence(self, nums):
        if len(nums)<2:
            return False
        nums.sort() # sort the array so we can check the common difference between every element.
        diff = nums[1]-nums[0]
        
        for i in range(2,len(nums)):
            if nums[i]-nums[i-1] != diff:
                return False
        return True