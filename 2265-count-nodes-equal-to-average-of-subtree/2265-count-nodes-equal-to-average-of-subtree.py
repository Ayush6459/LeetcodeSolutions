# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.count = 0
        def dfs(root):
            if not root:
                return (0,0)
            if not root.left and not root.right:
                self.count +=1
                return (root.val,1)
            if root.left and not root.right:
                x,nodecount= dfs(root.left)
                if (root.val+x)//(nodecount+1)==root.val:
                    self.count+=1
                return (root.val+x,nodecount+1)
            if not root.left and root.right:
                x,nodecount= dfs(root.right)
                if (root.val+x)//(nodecount+1)==root.val:
                    self.count+=1
                return (root.val+x,nodecount+1)
            if root.left and root.right:
                x,Lnodecount = dfs(root.left)
                y,Rnodecount = dfs(root.right)
                if (root.val +x+y)//(1+Lnodecount+Rnodecount) == root.val:
                    self.count+=1
                return (root.val+x+y,1+Lnodecount+Rnodecount)
        dfs(root)
        return self.count