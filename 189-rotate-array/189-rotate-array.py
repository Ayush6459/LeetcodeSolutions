class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %=len(nums)
        if k>0:
            self.reversed(nums,0,len(nums)-1)
            self.reversed(nums,0,k-1)
            self.reversed(nums,k,len(nums)-1)
            
        
    def reversed(self,arr,low,high):
        while low<=high:
            arr[low],arr[high]=arr[high],arr[low]
            low+=1
            high-=1
        
        
        