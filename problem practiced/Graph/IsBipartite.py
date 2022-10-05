def isBipartite(graph):
    col = [-1]*len(graph)

    def BFS(s):
        col[s] = 0
        q = []
        q.append(s)
        while q:
            u = q.pop(0)
            for v in graph[u]:
                if col[v] == -1:
                    col[v] = 1-col[u]
                    q.append(v)
                elif col[v] == col[u]:
                    return False
        return True

    for i in range(len(graph)):
        if col[i] ==-1:
            if not BFS(i):
                return False
    return True









