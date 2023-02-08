class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        '''
        # dp solution with O(n2) TC giving TLE
        n = len(nums)
        dp={}
        def fun(idx):
            if idx>=n:return False
            if idx == n-1:return True
            if nums[idx]==0:return False
            if idx in dp:return dp[idx]
            for i in range(1,nums[idx]+1):
                if fun(idx+i):
                    dp[idx] = True
                    return True
            return False
        
        return fun(0)
        '''
        
        # greedy solution
        
        goal = len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            if i+nums[i]>=goal:
                goal = i
        return True if goal == 0 else False
        