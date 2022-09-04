import collections
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res = []
        frontier = [(root, 0)]
        h = collections.defaultdict(list)
        while frontier:
            next = []
            for u, x in frontier:
                h[x].append(u.val)
                if u.left: next.append((u.left, x-1)) 
                if u.right: next.append((u.right, x+1))
                next.sort(key = lambda x: (x[1], x[0].val))
            frontier = next
        for k in sorted(h):
            res.append(h[k])
        return res