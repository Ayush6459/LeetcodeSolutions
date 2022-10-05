# Dfs approach for topological sort

from pydoc import visiblename


def TopologicalRec(graph,source,visited,stack):
    visited[source] = 1
    for v in graph[source]:
        if visited[v] == 0:
            TopologicalRec(graph,v,visited,stack)
    stack.append(source)
    return 

def ToplogicalSort(graph):
    visited = [0]*len(graph)
    stack = []
    for i in range(len(graph)):
        if visited[i] == 0:
            TopologicalRec(graph,i,visited,stack)
    print(visited)
    print(stack)

graph = [[1,2],[3],[],[],[5],[]]
ToplogicalSort(graph)
    