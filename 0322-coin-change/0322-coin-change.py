class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        
        def helper(amount):
            if amount == 0:
                return 0
            if amount in dp:return dp[amount]
            ans = sys.maxsize
            for coin in coins:
                if amount-coin>=0:
                    subproblem = helper(amount-coin)
                    if subproblem != -1:
                        ans = min(ans,subproblem+1)
                        
                    
            dp[amount] = ans if ans!=sys.maxsize else -1
            return dp[amount]
        return helper(amount)
            