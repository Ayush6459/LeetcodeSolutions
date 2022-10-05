from collections import deque


class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        d = {}
        stack = deque()

        for i in nums2[::-1]:
            # if the stack is empty
            if not stack:
                stack.append(i)
                d[i] = -1
            # if top is greater then curr element
            elif stack[-1] > i:
                d[i] = stack[-1]
                stack.append(i)
            elif stack[-1] <= i:
                while len(stack) and stack[-1] <= i:
                    stack.pop()
                if not stack:
                    d[i] = -1
                    stack.append(i)
                else:
                    d[i] = stack[-1]
                    stack.append(i)
        #print(d)
        res = []

        for i in nums1:
            if i in d:
                res.append(d[i])
        return res
