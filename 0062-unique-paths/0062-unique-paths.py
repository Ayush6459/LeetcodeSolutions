class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp with memoization 
        dpArr = [[-1 for _ in range(n)] for _ in range(m)]
        def usingMemoization(i,j):
            if i ==0 and j == 0:return 1
            if i<0 or j<0 : return 0
            if dpArr[i][j]!=-1:return dpArr[i][j]
            up = usingMemoization(i-1,j)
            left = usingMemoization(i,j-1)
            dpArr[i][j] = left + up 
            
            return left + up
        
        
        return  usingMemoization(m-1,n-1)
            
        