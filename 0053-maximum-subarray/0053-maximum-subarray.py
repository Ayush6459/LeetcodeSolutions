class Solution:
    def maxSubArray(self, arr: List[int]) -> int:
        res = arr[0]
        max_ending = arr[0]
        for i in range(1,len(arr)):
            max_ending = max(max_ending+arr[i],arr[i])
            res = max(max_ending,res)
        return res