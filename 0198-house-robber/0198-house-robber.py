class Solution:
    def rob(self, nums: List[int]) -> int:
        # using tabulation method 
        dp = [nums[0]]
        
        for i in range(1,len(nums)):
            pick = nums[i]
            if i>1:
                pick+=dp[i-2]
            notPick = dp[i-1]
            dp.append(max(pick,notPick))
        return dp[-1]
            
            
        