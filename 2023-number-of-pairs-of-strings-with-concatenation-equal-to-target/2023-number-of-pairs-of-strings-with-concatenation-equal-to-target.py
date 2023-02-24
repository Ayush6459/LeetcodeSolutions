class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                temp = nums[i]+nums[j]
                temp2 = nums[j]+nums[i]
                if temp == target:
                    count+=1
                if temp2 == target:
                    count+=1
        return count
            