# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = [0]
        if not root.left and not root.right:return root.val
        def dfs(root,currSum):
            if not root:return
            if not root.left and not root.right:
                #print(currSum)
                res[0]+=int(currSum)*10+root.val
                return
            dfs(root.left,currSum+str(root.val))
            dfs(root.right,currSum+str(root.val))
            return 
        dfs(root,'')
        return res[0]