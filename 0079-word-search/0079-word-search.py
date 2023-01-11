class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board) # row
        n = len(board[0]) # col
        lw = len(word)
        path = set()
        def backtrack(row,col,idx):
            if idx == lw:return True
            
            if (row<0 or col<0 or row>=m or col>=n or 
            word[idx]!=board[row][col] or (row,col) in path):
                return False
            path.add((row,col))
            res = (backtrack(row+1,col,idx+1) or 
                  backtrack(row-1,col,idx+1) or
                backtrack(row,col+1,idx+1) or
                backtrack(row,col-1,idx+1) )
            path.remove((row,col))
            return res
        
        for r in range(m):
            for c in range(n):
                if backtrack(r,c,0) : return True
        return False