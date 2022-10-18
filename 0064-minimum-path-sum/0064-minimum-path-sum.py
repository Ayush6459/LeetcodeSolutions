class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m , n = len(grid) , len(grid[0])
        prev = [0]*n
        
        for i in range(m):
            curr = [0]*n
            for j in range(n):
                if i==0 and j == 0 :
                    curr[j] = grid[i][j]
                    
                else:
                    up = left = float('inf')
                    if i>0:
                        up = grid[i][j] + prev[j]
                        
                    if j>0:
                        left = grid[i][j] + curr[j-1]
                        
                    curr[j] = min(up,left)
                    
            prev = curr 
            
        return prev[-1]