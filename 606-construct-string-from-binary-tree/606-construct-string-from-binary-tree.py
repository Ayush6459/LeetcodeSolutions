# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def solve(root,s):
            if not root:
                return
            if not root.left and not root.right:
                s.append(str(root.val))
            
            if not root.left and root.right:
                s.append(str(root.val))
                s.append("()(")
                solve(root.right,s)
                s.append(")")
            if root.left:
                s.append(str(root.val))
                s.append("(")
                solve(root.left,s)
                s.append(")")
                if root.right:
                    s.append("(")
                    solve(root.right,s)
                    s.append(")")
                    
            return s
        
        s = []
        solve(root,s)
        
                
        return ''.join(s)
            
            