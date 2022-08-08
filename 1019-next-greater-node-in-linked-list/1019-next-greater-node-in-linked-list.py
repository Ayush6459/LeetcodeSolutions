# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        stack = []
        res = []
        values = []
        curr = head
        while curr:
            values.append(curr.val)
            curr = curr.next
        
        for i in values[::-1]:
            if not stack :
                stack.append(i)
                res.append(0)
            elif stack[-1]>i:
                res.append(stack[-1])
                stack.append(i)
            else:
                while stack and stack[-1]<=i:
                    stack.pop()
                if not stack:
                    res.append(0)
                    stack.append(i)
                else:
                    res.append(stack[-1])
                    stack.append(i)
        '''
        
        while curr:
            if not stack :
                stack.append(curr.val)
                res.append(0)
            elif stack[-1]>curr.val:
                res.append(stack[-1])
                stack.append(curr.val)
            else:
                while stack and stack[-1]<=curr.val:
                    stack.pop()
                if not stack:
                    res.append(0)
                    stack.append(curr.val)
                res.append(stack[-1])
                stack.append(curr.val)
            
            curr = curr.next
            '''
        return res[::-1]
        
    def reverseList(self,head):
        # Code here
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev