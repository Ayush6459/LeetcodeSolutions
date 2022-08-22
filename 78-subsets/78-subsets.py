class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        def solve(arr,index,subarr):
            if index==len(arr):
                self.res.append(subarr)
            else:
                solve(arr,index+1,subarr)
                solve(arr,index+1,subarr+[arr[index]])
        solve(nums,0,[])
        return self.res