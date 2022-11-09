# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = [root]
        ans = []
        
        while q:
            temp = []
            maxi = float('-inf')
            for node in q:
                maxi = max(maxi,node.val)
                temp.extend([node.left,node.right])
            q = [i for i in temp if i]
                    
            ans.append(maxi)
        return ans