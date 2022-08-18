# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
import sys
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = deque()
        res = [-sys.maxsize-1,-sys.maxsize-1]
        level = 0
        if not root:
            return 0
        q.append(root)
        while q:
            s = 0
            size = len(q)
            for _ in range(size):
                x = q.popleft()
                s+=x.val
                if x.left:q.append(x.left)
                if x.right:q.append(x.right)
                    
            level+=1
            # check for if the current level is greater than or not 
            if res[0]<s:
                res=[s,level]
        return res[1]