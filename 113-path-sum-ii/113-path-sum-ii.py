# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res =[]
        self.solve(root,targetSum,res,[])
        return res
    
    def solve(self,root, target,res,currpath):
        if not root:
            return
        if not root.left and not root.right:
            if sum(currpath+[root.val])==target:
                res.append(currpath+[root.val])
        self.solve(root.left,target,res,currpath+[root.val])
        self.solve(root.right,target,res,currpath+[root.val])
        