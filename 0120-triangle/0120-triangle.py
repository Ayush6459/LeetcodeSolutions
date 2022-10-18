class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle[-1])
        dp = [[-1 for _ in i] for i in triangle]
        
        def Memoization(i,j):
            if  i == n-1 :
                return triangle[n-1][j]
            if dp[i][j]!=-1 : return dp[i][j]
            
            d = triangle[i][j] + Memoization(i+1,j)
            dg = triangle[i][j] + Memoization(i+1,j+1)
            
            dp[i][j] = min(d,dg)
            return dp[i][j]
        
        return Memoization(0,0)