class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        firstOccr = self.FindFirstIndex(nums,target)
        lastOccr = self.FindLastIndex(nums,target)
        #print(firstOccr,lastOccr)
        if firstOccr == -1 or lastOccr == -1:
            return []
                
        return list(range(firstOccr,lastOccr+1))
        
        
        
    def FindFirstIndex(self,nums,target):
        low = 0 
        high = len(nums)-1
        res = -1
        while low<=high:
            mid = (high+low)//2
            if nums[mid]==target:
                res = mid
                high = mid-1
            elif nums[mid]>target:
                high = mid -1
            else:
                low = mid+1
        return res
    def FindLastIndex(self,nums,target):
        low = 0
        high = len(nums)-1
        res = -1
        while low<=high:
            mid = (low+high)//2
            if nums[mid]==target:
                res = mid
                low = mid+1
            elif nums[mid]<target:
                low = mid+1
            else:
                high = mid -1
        return res
                        