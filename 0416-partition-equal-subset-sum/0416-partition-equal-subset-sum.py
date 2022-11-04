class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        def haveTargetSumSubset(index,target):
            if target == 0 : return True
            if index == 0 :
                return nums[index] == target 
            if dp[index][target] != -1 : return dp[index][target]
            pick = False
            if target >= nums[index]:
                pick = haveTargetSumSubset(index-1,target-nums[index])
            notpick = haveTargetSumSubset(index-1,target)
            dp[index][target] = pick or notpick 
            return dp[index][target]
        
        s = sum(nums) 
        if s%2 !=0 : return False 
        target = s//2
        dp = [[-1 for _ in range(target+1)] for _ in range(len(nums))]
        
        return haveTargetSumSubset(len(nums)-1,target)