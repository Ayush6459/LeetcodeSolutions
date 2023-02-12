"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        q = collections.deque()
        if not root:return None
        q.append(root)
        while q:
            level = []
            for i in range(len(q)):
                node = q.popleft()
                if node.left:q.append(node.left)
                if node.right:q.append(node.right)
                if level:
                    level[-1].next = node
                level.append(node)
            
        return root