# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def depth(root):
            
            nonlocal maxDiameter
            if not root: 
                return 0
            left = depth(root.left)
            right = depth(root.right)
            
            #get the no of edges in both children
            currentDiameter = left + right
            
            #track max diameter
            maxDiameter = max(maxDiameter, currentDiameter)
            
            #we can only return one of the children
            #we add a one to represent the edge 
            #between node and parent above
            return max(left, right) + 1
        
        maxDiameter = 0
        depth(root)
        return maxDiameter