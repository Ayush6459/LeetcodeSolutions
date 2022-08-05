class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        right = self.nextSmallerRight(heights)
        left = self.nextSmallerLeft(heights)
        width =[x-y-1 for x,y in zip(right,left)]
        area = [x*y for x,y in zip(heights,width)]
        return max(area)
        
    def nextSmallerRight(self,nums):
        stack = []
        res = []
        psuedoIndex = len(nums)
        for i in range(len(nums)-1,-1,-1):
            if not stack :
                res.append(psuedoIndex)
            elif stack[-1][0]<nums[i]:
                res.append(stack[-1][1])
            else:
                while stack and stack[-1][0]>=nums[i]:
                    stack.pop()
                if not stack:
                    res.append(psuedoIndex)
                else:
                    res.append(stack[-1][1])
            stack.append([nums[i],i])
        return res[::-1]
    
    def nextSmallerLeft(self,nums):
        stack =[]
        res  = []
        psuedoIndex = -1
        for i in range(len(nums)):
            if not stack :
                res.append(psuedoIndex)
            elif stack[-1][0] <nums[i]:
                res.append(stack[-1][1])
            else:
                while stack and stack[-1][0]>=nums[i]:
                    stack.pop()
                if not stack:
                    res.append(psuedoIndex)
                else:
                    res.append(stack[-1][1])
            stack.append([nums[i],i])

        return res