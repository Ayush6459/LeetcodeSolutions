class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        zeroCount = nums.count(0)
        if zeroCount>1:
            return [0]*len(nums)
        product = 1
        res = []
        
        if zeroCount==1:
            for i in nums:
                if i!=0:
                    product*=i
            for i in nums:
                if i == 0:
                    res.append(product)
                else:
                    res.append(0)
            return res
        else:
            product = 1
            res = []
            for i in nums:
                product*=i
            for i in nums:
                res.append(product/i)
            return res
                
                
        