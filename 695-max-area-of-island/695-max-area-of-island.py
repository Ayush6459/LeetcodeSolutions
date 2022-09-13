class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def markIsland(i,j,row,col):
            if i<0 or i>=row or j<0 or j>=col or grid[i][j]==0:
                return 0
            grid[i][j]=0
            x= markIsland(i-1,j,row,col)
            y =markIsland(i+1,j,row,col)
            a = markIsland(i,j-1,row,col)
            b = markIsland(i,j+1,row,col)
            return 1+x+y+a+b
        
        ans = 0
        row = len(grid)
        col = len(grid[0])
        for curRow in range(row):
            for curCol in range(col):
                if grid[curRow][curCol]==1:
                    
                    ans = max(ans,markIsland(curRow,curCol,row,col))
        return ans