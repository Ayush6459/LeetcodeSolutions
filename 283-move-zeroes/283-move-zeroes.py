class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        first = 0
        second =0
        while first < len(nums) and second <len(nums):
            if nums[second]!=0:
                nums[first],nums[second] = nums[second],nums[first]
                first+=1
            second+=1