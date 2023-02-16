class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        dx = [-1,0,1,0]
        dy = [0,-1,0,1]
        startpixel = image[sr][sc]
        def isvalid(i,j):
            # this function is to check for vaild indexes
            if i<0 or i>=m or j<0 or j>=n:return False
            if image[i][j] == color or image[i][j]!= startpixel :return False
            
            return True
        
        def dfs(i,j):
            # traverse through all the connected cells and modify the image data
            image[i][j] = color
            for x,y in zip(dx,dy):
                if isvalid(i+x,j+y):
                    dfs(i+x,j+y)
            return 
        
        dfs(sr,sc)
        return image