import sys
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        maxi = -sys.maxsize - 1
        
        def dfs(root,maxi):
            nonlocal count
            if not root:
                return
            if root.val>=maxi:
                maxi = root.val
                count+=1
            dfs(root.left,maxi)
            dfs(root.right,maxi)
        dfs(root,maxi)
        return count