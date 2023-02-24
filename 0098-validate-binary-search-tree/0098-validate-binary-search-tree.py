# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            if not root:return (float('-inf'),float('inf'),True)
            leftMax, leftMin, isLeftBST = dfs(root.left)
            rightMax, rightMin, isrightBST = dfs(root.right)
            
            if isLeftBST and isrightBST and leftMax<root.val and root.val<rightMin:
                return (max(root.val,rightMax), min(root.val,leftMin), True)
            
            return (float('inf'),float('inf'),False)
        
        x = dfs(root)
        return x[2]