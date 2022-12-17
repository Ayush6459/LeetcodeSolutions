class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        x = sorted(nums)
        
        d = dict()
        for idx,i in enumerate(x):
            if i not in d:
                d[i] = idx
        return [d[i] for i in nums]