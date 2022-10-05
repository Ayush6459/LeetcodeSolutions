# detect Cycle using dfs algo

''' 
    the trick is to maintain the parent of the current recursive call
'''



def dfsDetectRec(adj,s,visited,recstk): # this work for checking the cycle for all the connected node from a given source node
    visited[s] = True # make the current node as visited
    recstk[s] = True  # mark the current value as true for current recursion stack
    for v in adj[s] :
        # check if the current adjecent node is visted or not 
        # if the node is not visted then call for the function for the current not visited node
        if visited[v]==False and dfsDetectRec(adj,v,visited,recstk):
            return True 
        elif recstk[v] == True :# this means that element is alredy in the recusion cycle and have been visited before 
            return True         # there will be cycle 
        
    recstk[s] = False # remove the current element of the current recursion cycle
    return False # there is no cycle in graph

# to check the cycle for all the component we have to go through all the nodes in the graph and check for the cycle
# by calling the above function 
# we will call the function for any node if that node is not visited yet

def dfsDetectMain(graph:list,V:int):
    visited = [False]*V 
    recstk = [False]*V 
    for u  in range(V): # the graph is zero indexed here and the representation is of adjacency list type 
        if visited[u] == False and dfsDetectRec(graph, u, visited, recstk):
            return True 
    return False 



'''
Detect cycle using bfs approach 
Intution : We are going to use khan's algo of topological sort to detect cycle 
For any Directed cyclic graph it this algo will not able to visite all the node and hence we can prove that there is a cycle in graph
'''

def bfsDetectCycle(adj:list,V:int,indegree:list):
    '''
        adj : adjacency list
        V: number of vertices in graph
        indegree: array containing all the indegree value of every vertices 
    '''

    # create a queue to store all the nodes whose indegree are 0
    q = []
    for i in range(V):
        if indegree[i] == 0:
            q.append(i)
    # make a counter variable to keep track of number of nodes visited 
    count = 0 
    while q:
        u = q.pop(0) # pop the first element from the q 
        #print(u)
        for v in adj[u]:
            indegree[v]-=1
            if indegree[v]==0:
                q.append(v)
        count+=1

    return count!=V 

def calIndegree(adj):
    indegree = [0]*len(adj)    
    for u in adj:
        for v in u:
            indegree[v]+=1
    return indegree 

if __name__ == '__main__':
    graph =  [[6,7],[2,4,6],[],[4,0],[],[1],[],[1,0]]
    indegree = calIndegree(graph)
    #print(indegree)
    #print(bfsDetectCycle(graph,len(graph),indegree))

    print(dfsDetectMain(graph,len(graph)))
