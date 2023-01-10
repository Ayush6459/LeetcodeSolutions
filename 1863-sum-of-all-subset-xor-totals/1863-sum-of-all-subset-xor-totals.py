class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        sum = [0]
        n = len(nums)
        def XOR(arr):
            temp = 0
            for i in arr:
                temp= temp^i
            return temp
        def backtrack(idx,lst):
            if idx>n-1:
                sum[0]+=XOR(lst)
                return 
            else:
                backtrack(idx+1,lst+[nums[idx]])
                backtrack(idx+1,lst)
                return
        backtrack(0,[])
        return sum[0]
        