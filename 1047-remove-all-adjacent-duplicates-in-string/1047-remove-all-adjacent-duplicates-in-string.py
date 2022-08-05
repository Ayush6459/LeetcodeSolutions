from collections import deque
class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = deque()
        r = ''
        n = len(s)-1
        for i in range(len(s)):
            # check if stack is empty 
            # if empty just put the element in that 
            if not stack :
                stack.append(s[i])
            else:
                # check if the current element is equal to the top of the stack or not
                # if equal pop the element till the stack top not equal to the curr elemnet or
                # stack become empty
                # and if stack top not equal to the top put the curr elemnet in stack
                
                if stack[-1]!=s[i]:
                    stack.append(s[i])
                else:
                    while stack and stack[-1]==s[i]:
                        stack.pop()
                    if i==n and not stack:
                        stack.append(s[i])
        
        if len(stack)==1 and len(s)%2==0:
            return ''
            
        
        while stack :
            r+=stack.pop()
        return r[::-1]
            
                
                    
        