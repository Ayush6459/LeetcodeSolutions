class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def markIsland(i,j,row,col):
            if i<0 or i>=row or j<0 or j>=col or grid[i][j]=='0':
                return 
            grid[i][j]='0'
            markIsland(i-1,j,row,col)
            markIsland(i+1,j,row,col)
            markIsland(i,j-1,row,col)
            markIsland(i,j+1,row,col)
            
        ans = 0
        row = len(grid)
        col = len(grid[0])
        for curRow in range(row):
            for curCol in range(col):
                if grid[curRow][curCol]=='1':
                    ans+=1
                    markIsland(curRow,curCol,row,col)
        return ans