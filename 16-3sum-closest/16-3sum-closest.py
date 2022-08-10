import sys
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        
        result = float("inf")
        min_diff = float("inf")
        length = len(nums)
        for i in range(length-2):
            j = i+1
            k = length-1
            while j<k:
                diff = nums[i]+nums[j]+nums[k] - target
                if abs(diff)<min_diff:
                    min_diff = abs(diff)
                    result = nums[i]+nums[j]+nums[k]
                elif diff <0 :
                    j+=1
                elif diff>0:
                    k-=1
                else:
                    return target
        return result
        