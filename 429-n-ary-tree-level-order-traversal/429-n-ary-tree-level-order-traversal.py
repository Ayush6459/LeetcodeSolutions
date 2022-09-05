"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        res = []
        q = []
        q.append(root)
        while q:
            temp = []
            size = len(q)
            for i in range(size):
                x=q.pop(0)
                temp.append(x.val)
                while x.children:
                    q.append(x.children.pop(0))
                    
            res.append(temp)
        return res