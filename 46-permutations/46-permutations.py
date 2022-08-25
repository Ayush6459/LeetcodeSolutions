class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        if (len(nums)==1):
            return [nums[:]]
        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)
            for i in perms:
                i.append(n)
            result.extend(perms)
            nums.append(n)
        return result