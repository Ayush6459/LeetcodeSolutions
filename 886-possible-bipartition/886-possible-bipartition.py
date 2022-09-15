class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        
        graph = [[] for i in range(n)]
        for i in dislikes:
            graph[i[0]-1].append(i[1]-1)
            graph[i[1]-1].append(i[0]-1)
        
        
        return self.isBipartite(graph)
        
    def isBipartite(self, graph):
        col = [-1]*len(graph)
        
        def BFS(s):
            col[s] = 0
            q = []
            q.append(s)
            while q:
                u = q.pop(0)
                for v in graph[u]:
                    if col[v]==-1:
                        col[v]=1-col[u]
                        q.append(v)
                    elif col[v]==col[u]:
                        return False
            return True
        
        for i in range(len(graph)):
            if col[i]==-1:
                if not BFS(i):
                    return False
        return True