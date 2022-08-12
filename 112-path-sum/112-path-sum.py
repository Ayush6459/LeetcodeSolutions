# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.dfs(root,0,targetSum)
    
    def dfs(self,root,curr_sum,target):
        if not root:
            return False 
        curr_sum +=root.val
        if not root.left and not root.right :
            if curr_sum == target:
                return True
            else:
                return False
        return self.dfs(root.left,curr_sum,target) or self.dfs(root.right,curr_sum,target)