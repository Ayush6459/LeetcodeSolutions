'''
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.
Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
'''
# INTUTION  : 

# Step1 : Make a adjacancy list graph from the given list
# Step2 : Find the total number of component in the graph by traversing the graph this will be our total no. of Provinces

def makeGraph(arr):
    graph = []
    for i in range(len(arr)):
        graph.append([])
    
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if i!=j and arr[i][j]==1:
                graph[i].append(j)

    return graph 

def dfs(adj,visited,s):
    visited[s] = True 
    for i in adj[s]:
        if visited[i] == False :
            dfs(adj,visited,i)

def dfsMain(adj, V):
    visited = [False]*V 
    count = 0
    for i in range(V):
        if visited[i]==False:
            count+=1
            dfs(adj,visited,i)
    return count 

if __name__ == "__main__":
    arr = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    graph = makeGraph(arr)
    print(dfsMain(graph,len(graph)))
