def Solve(board,col,n):
    # base condition 
    if col==n:
        print(board)
        print('\n')
        return 1
    ways = 0
    for i in range(n):
        if isSafe(board,i,col,n):
            board[i][col]=1
            ways+=Solve(board,col+1,n)
            board[i][col]=0
    return ways

def isSafe(board,row,col,n):
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
    return True


board = []
n=4

for i in range(n):
    board.append([])
    for j in range(n):
        board[-1].append(0)

print(board)
print('\n')
print(Solve(board,0,4))

