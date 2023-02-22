"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque 
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node : return 
        visited = {}
        '''
        def DFS(node:'Node') -> 'Node':
            clone = Node(node.val) # make a new tree node
            # add the current node in visited
            visited[node.val] = clone
            # traverse the neighbors 
            for v in node.neighbors:
                if v.val in visited:
                    clone.neighbors.append(visited[v.val])
                else:
                    clone.neighbors.append(DFS(v))   
            return clone'''
        
        def bfs(node):
            q = deque([node])
            clone = {node.val:Node(node.val)}
            while q:
                curr = q.popleft()
                curr_clone = clone[curr.val]
                for v in curr.neighbors:
                    if v.val not in clone:
                        clone[v.val]= Node(v.val)
                        q.append(v)
                    curr_clone.neighbors.append(clone[v.val])
            return clone[node.val]
        return bfs(node)
            