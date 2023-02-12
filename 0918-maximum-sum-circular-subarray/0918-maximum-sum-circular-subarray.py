from collections import deque
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # most efficient way to solve this problem 
        arrsum = 0
        maxsum = float('-inf')
        minsum = float('inf')
        maxending, minending = 0, 0
        for i in nums:
            arrsum+=i
            maxending+=i
            maxsum = maxending if maxsum<maxending else maxsum
            maxending = 0 if maxending<0 else maxending
            minending+=i
            minsum = minending if minsum>minending else minsum
            minending = 0 if minending>0 else minending
            
        if arrsum == minsum:return maxsum
        return max(maxsum,arrsum-minsum)
        
        
        '''# O(n^2) solution  gives TLE
        d = deque(nums)
        res = float('-inf')
        for i in range(len(nums)):
            res = max(res,self.kadensAlgo(d))
            x = d.popleft()
            d.append(x)
        return res
        
    def kadensAlgo(self,arr):
        maxsofar = float('-inf')
        maxending = 0
        
        for i in arr:
            maxending+=i
            if maxsofar<maxending:
                maxsofar = maxending
            if maxending <0:
                maxending = 0
        return maxsofar'''
        
    