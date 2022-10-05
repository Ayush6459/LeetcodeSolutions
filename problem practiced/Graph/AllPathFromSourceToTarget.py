'''
Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.

The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).


'''

def dfs(adj,currIndex,lastIndex,visited,res):
    if visited[-1]==lastIndex:
        res.append(visited)
        return 
    for v in adj[currIndex]:
        dfs(adj,v,lastIndex,visited+[v],res)
    return res

graph = [[1,2],[3],[3],[]]
v = [0]
res = dfs(graph,0,len(graph)-1,v,[])
print(res)
