# for connected component

def dfsConnected(adj,visited,s,dest):
    visited[s] = 1
    if s == dest:
        print('yes')
        return True 
    #print(s)
    for v in adj[s]:
        if visited[v]==0:
            dfsConnected(adj,visited,v,dest)

    #print('False')
    return 


adj = [[1, 2], [0], [0], [4, 5], [3, 5], [3, 4]]
v = [0]*6

dfsConnected(adj,v,0,3)


def hasPath(self, graph, src, dst, visited):
    if src == dst:
        return True
    if src in visited:
        return False
    visited.add(src)
    for neighbour in graph[src]:
        if self.hasPath(graph, neighbour, dst, visited) == True:
            return True
    return False
