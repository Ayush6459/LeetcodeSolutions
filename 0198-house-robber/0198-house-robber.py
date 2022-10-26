class Solution:
    def rob(self, nums: List[int]) -> int:
        # using memoization technique
        dp = [-1]*len(nums)
        def memo(index):
            if index==0:return nums[index]
            if index<0: return 0
            if dp[index]!= -1:
                return dp[index]
            pick = nums[index] + memo(index-2)
            notPick = memo(index-1)
            dp[index] = max(pick,notPick)
            return dp[index]
        return memo(len(nums)-1)
        