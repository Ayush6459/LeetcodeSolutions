class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        i,j,res= 0,0,0
        while i<len(nums):
            if nums[i]!=0:
                i+=1
            else:
                j = i+1
                while j<len(nums):
                    if nums[j]==0:
                        j+=1
                    else:
                        break
                res+=((j-i)*(j-i+1))//2
                i = j+1
        return res