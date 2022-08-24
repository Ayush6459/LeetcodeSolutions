class Solution:
    def totalNQueens(self, n: int) -> int:
        def validMove(board,row,col):
            i=col
            while i>=0:
                if board[row][i]:
                    return False
                i-=1
            i=row
            j=col
            while (i>=0 and j>=0):
                if board[i][j]:
                    return False
                i-=1
                j-=1
            i=row
            j=col
            while (i<n and j>=0):
                if board[i][j]:
                    return False
                i+=1
                j-=1
            return True
        def solve(board,col):
            if (col==n):
                res[0]+=1
                return
            for i in range(n):
                if validMove(board,i,col):
                    board[i][col]=1
                    solve(board,col+1)
                    board[i][col]=0
            return
        
        res=[0]
        board=[]
        for i in range(n):
            board.append([])
            for j in range(n):
                board[-1].append(0)
        solve(board,0)
        return res[0]
        
        
    '''# main solve function to find the solution
    def Solve(self,board,col,n):
        # base condition 
        if col==n:
            print(board)
            self.res[0]+=1
            return 1
        ways = 0
        for i in range(n):
            if self.isSafe(board,i,col,n):
                board[i][col]=1
                ways+=self.Solve(board,col+1,n)
                board[i][col]=0
        return ways
    
    
    # utility function to check if the placment is safe or not 
    def isSafe(self,board,row,col,n):
        # check if the previous columns value in this row
        for j in range(col):
            if board[row][j]==1:
                return False
        
        # check for upper left
        for i,j in zip(range(row,-1,-1),range(col,-1,-1)):
            if board[i][j]==1:
                return False
        #check for lower left
        for i,j in zip(range(row,n,1),range(col,-1,-1)):
            if board[i][j]==1:
                False
        # otherwise return True
        return True'''