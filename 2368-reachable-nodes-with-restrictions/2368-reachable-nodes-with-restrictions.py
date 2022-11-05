class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        
        def makegraph():
            graph = [[] for _ in range(n)]
            for u, v in edges:
                graph[u].append(v)
                graph[v].append(u)
                
            return graph
        graph = makegraph()
        
        ans = 1
        restricted = set(restricted)
        visited = set()
        visited.add(0) # add 0th node as a visited node 
        q = [0] # put the 0th node in queue 
        while q :
            u = q.pop(0)
            for v in graph[u]:
                if v not in visited and v not in restricted :
                    q.append(v)
                    visited.add(v)
                    ans+=1
                    
        return ans
                    
            
        