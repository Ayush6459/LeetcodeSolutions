# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if root==None:
            return None
        _l = self.pruneTree(root.left)
        _r = self.pruneTree(root.right)
        if root.val == 0 and _l == None and _r == None:
            return None
        else:
            root.left = _l
            root.right = _r
        return root
    
        