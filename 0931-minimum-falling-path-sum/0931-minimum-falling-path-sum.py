class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        # memoized solution 
        # make a dp table 
        m = len(matrix[0]) # col count
        n = len(matrix) # row count
        dp = [[float('inf') for _ in range(m)] for _ in range(n)] 
        
        def Reccurence(i,j):
            # Base Case 1 :- if we reach the last row
            if i == n-1 and 0<=j<m:
                return matrix[i][j]
            
            # Base case 2 :- If we go out of bound 
            if j < 0 or j > m-1:
                return float('inf')
            
            # check if we have already visited the current state 
            if dp[i][j] != float('inf') : return dp[i][j]
            
            # we have three choices here 
            # 1:- we go down straight from current cell
            # 2:- we go down diagonally left from current cell
            # 3:- we go down diagonally right from current cell
            down = matrix[i][j] + Reccurence(i+1, j)
            left = matrix[i][j] + Reccurence(i+1, j-1)
            right = matrix[i][j] + Reccurence(i+1, j+1)
            
            dp[i][j] = min(down,left,right)
            return dp[i][j]
        
        currmin = float('inf')
        for j in range(m):
            currmin = min(currmin,Reccurence(0, j))
        return currmin