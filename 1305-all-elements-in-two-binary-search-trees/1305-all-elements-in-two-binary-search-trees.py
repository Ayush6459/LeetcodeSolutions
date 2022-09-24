# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        l1 = self.inorder(root1,[])
        l2 = self.inorder(root2,[])
        if l1 and not l2:
            return l1
        if l2 and not l1:
            return l2
        return sorted(l1+l2)
        
    def inorder(self,root,res):
        if not root:
            return 
        self.inorder(root.left,res)
        res.append(root.val)
        self.inorder(root.right,res)
        return res
        