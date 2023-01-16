class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        return self.memoization(coins,amount)
    def memoization(self, coins: List[int], amount: int) -> int:
        dp = {}
        
        def dfs(amount):
            if amount in dp:
                return dp[amount]
            if amount == 0:
                return 0
            
            res = math.inf
            for coin in coins:
                if (amount - coin) >= 0:
                    res = min(res,1 + dfs(amount - coin))
            dp[amount] = res
            return res
        
        res = dfs(amount)
        return res if res != math.inf else -1