class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # bottom up approach
        dp = {}
        dp[0] = 0
        for i in range(1,amount+1):
            dp[i] = sys.maxsize
            for coin in coins:
                if i-coin>=0:
                    subproblem = dp[i-coin]
                    if subproblem != -1:
                        dp[i] = min(dp[i],subproblem+1)
            dp[i] = dp[i] if dp[i]!=sys.maxsize else -1
        return dp[amount]
         
            