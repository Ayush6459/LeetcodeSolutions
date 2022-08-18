# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # method 1
        if not root :return[]
        q = deque()
        reverse = False
        q.append(root)
        res1=[]
        while q:
            count = len(q)
            temp = []
            for i in range(count):
                x = q.popleft()
                temp.append(x.val)
                if x.left:q.append(x.left)
                if x.right:q.append(x.right)
            
            if reverse:res1.append(reversed(temp))
            else:
                res1.append(temp)
            reverse = not reverse
        return res1
        
    
        '''
        s1 = deque() 
        s2 = deque()
        # check if root is empty
        if not root:
            return []
        """
            idea : 
                first put the root in first stack s1
                now traverse till any of the stack is not empty
                    while s1 is not empty 
                        a. take out the node and store it in result
                        b. push the children to in s2
                    while s2 is not empty 
                        a. take out the node and store it in result
                        b. push the childrens to in s1
        """
        res = []
        s1.append(root)
        while s1 or s2:
            if s1:
                temp =[]
                while s1:
                    x = s1.pop()
                    temp.append(x.val)
                    if x.left: 
                        s2.append(x.left)
                    if x.right:
                        s2.append(x.right)
                res.append(temp)
            if s2:
                temp = []
                while s2:
                    x = s2.pop()
                    temp.append(x.val)
                    if x.right:
                        s1.append(x.right)
                    if x.left:
                        s1.append(x.left)
                res.append(temp)
                
        return res
        '''
        