# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        ans = 0
        
        def bfs(root):
            if root is None :return
            q  = [root]
            prev = []
            while q:
                
                temp = []
                for i in q:
                    temp.extend([i.left,i.right])
                prev = q[:]
                q = [i for i in temp if i]
                
            return prev[0].val
        return (bfs(root))
            
        
                