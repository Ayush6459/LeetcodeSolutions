from typing import List


def BFS(adj : List[List],V:int):
    visited = [0]*V
    count = 0
    for i in range(V):
        if visited[i]==0:
            count+=1
            q = []
            visited[i]=1 
            q.append(i)
            while q:
                u = q.pop(0)
                print(u)
                for v in adj[u]:
                    if visited[v]==0:
                        visited[v]=1
                        q.append(v)
    print(count)
    return 

adj = [[1,2],[0],[0],[4,5],[3,5],[3,4]]
edge = [[0,1],[0,2],[3,5],[5,4],[4,3]]
v = 6
graph = [[] for i in range(v)] 
for u,v in edge:
    graph[u].append(v)
    graph[v].append(u)
print(graph)



BFS(adj,v)
#print(adj[1])