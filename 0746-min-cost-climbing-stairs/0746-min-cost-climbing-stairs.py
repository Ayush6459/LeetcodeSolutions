class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) <= 2:
            return min(cost)
        else:
            dp = [-1]*len(cost)
            def calMincost(index):
                if index >= len(cost):
                    return 0
                if dp[index]!=-1:return dp[index]
                singleStep = cost[index] + calMincost(index+1)
                
                doubleStep = cost[index] + calMincost(index+2)
                dp[index] = min(singleStep , doubleStep)
                return dp[index]
            
            return min(calMincost(0), calMincost(1))
    
    