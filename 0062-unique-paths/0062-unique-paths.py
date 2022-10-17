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
        
        
        #return  usingMemoization(m-1,n-1)
    
        def usingTabulation():
            dpArr[0][0] = 1
            for i in range(0,m):
                for j in range(0,n):
                    if i ==0 and j == 0:continue
                        
                    else:
                        up = left = 0
                        if i>0:
                            up = dpArr[i-1][j]
                        if j>0:
                            left = dpArr[i][j-1]
                        dpArr[i][j] = up+left
                        
            return dpArr[m-1][n-1]
        return usingTabulation() 
        