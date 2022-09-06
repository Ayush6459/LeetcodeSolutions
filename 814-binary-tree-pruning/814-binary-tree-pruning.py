# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
         return root if self.fun(root) else None
            
    def fun(self,root):
        if not root:
            return False
        left = self.fun(root.left)
        right = self.fun(root.right)
        if not left:
            root.left = None
        if not right:
            root.right=None
        return root.val or left or right
    
        