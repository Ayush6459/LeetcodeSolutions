# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        ans,level = [],[root]
        while level:
            ans.append(sum([node.val for node in level])/len(level))
            temp = []
            for node in level:
                temp.extend([node.left,node.right])
            level = [leaf for leaf in temp if leaf]
        return ans