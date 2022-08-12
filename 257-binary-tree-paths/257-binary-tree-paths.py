# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        if not root:
            return []
        self.dfs(root,'',res)
        return res
    
    def dfs(self,root,path,res):
        if not root:
            return
        if not root.left and not root.right:
            res.append(path+str(root.val))
        self.dfs(root.left,path+str(root.val)+'->',res)
        self.dfs(root.right,path+str(root.val)+'->',res)