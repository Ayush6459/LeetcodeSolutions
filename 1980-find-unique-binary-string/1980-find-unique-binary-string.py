class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums[0])
        nums = set(nums)
        mini = '0'*n
        maxi = '1'*n
        if mini not in nums:
            return mini
        if maxi not in nums:
            return maxi
        for i in range(int(maxi,2)+1):
            x = f'{i:0{n}b}'
            if x not in nums:
                return x