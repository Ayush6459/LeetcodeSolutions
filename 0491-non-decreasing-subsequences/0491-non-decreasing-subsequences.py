class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = set()
        
        def backtrack(idx,lst):
            if idx>=n:
                if tuple(lst) not in res and len(lst)>=2:
                    res.add(tuple(lst))
                return 
            if lst and lst[-1]>nums[idx]:
                backtrack(idx+1,lst)
            else:
                backtrack(idx+1,lst+[nums[idx]])
                backtrack(idx+1,lst)
            return 
        backtrack(0,[])
        
        return res