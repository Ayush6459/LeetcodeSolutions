class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        s = 0
        nums.sort()
        i = 0
        j = len(nums)-1
        while (i+2) <= j:
            s +=nums[j-1]
            j = j-2
            i = i+1
        return s
        