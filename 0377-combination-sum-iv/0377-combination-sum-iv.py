class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = {}
        def helper(amount):
            if amount<0:return 0
            if amount == 0:return 1
            if amount in dp:return dp[amount]
            ans = 0
            for i in nums:
                ans+=helper(amount-i)
            dp[amount] = ans
            return dp[amount]
        return helper(target)