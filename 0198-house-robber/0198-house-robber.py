class Solution:
    def rob(self, nums: List[int]) -> int:
        # using tabulation method and space optimization
        prev2 = 0
        prev = nums[0]
        for i in range(1,len(nums)):
            take = nums[i]
            if i>1:
                take+=prev2
            nontake = prev
            curr = max(take,nontake)
            prev2 = prev
            prev = curr
            
        return prev
            
            
        