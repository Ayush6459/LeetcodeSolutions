class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        negCount = 0
        for i in grid:
            negIndex = self.FirstNegativeIndex(i)
            if negIndex>=0:
                negCount+=(n-negIndex)
        return negCount
        
    def FirstNegativeIndex(self,arr):
        low = 0
        high = len(arr)-1
        ans = -1
        while low <= high:
            mid = (low+high)//2
            if arr[mid]<0:
                ans = mid
                high = mid - 1
            else:
                low = mid+1
        return ans
            
            