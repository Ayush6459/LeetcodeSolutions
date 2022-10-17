class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m , n = len(obstacleGrid) , len(obstacleGrid[0])
        dp = [[-1 for _ in range(n)] for _ in range(m)] 
        
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1: dp[i][j] = 0
                elif i == 0 and j == 0 :
                    dp[i][j] = 1
                else:
                    up = left = 0
                    if i>0:
                        up = dp[i-1][j]
                    if j>0:
                        left = dp[i][j-1]
                        
                    dp[i][j] = up + left
                    
        return dp[m-1][n-1]
                        