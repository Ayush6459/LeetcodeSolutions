class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = self.makeGraph(prerequisites,numCourses)
        visited = [False]*numCourses
        recstk = [False]*numCourses
        #print(graph)
        for i in range(numCourses):
            if visited[i]==False:
                if self.checkCycle(graph,i,visited,recstk):
                    return False
                
        return True
        
    def makeGraph(self,edges,vertex):
        graph = [[] for i in range(vertex)]
        for x,y in edges:
            graph[y].append(x)
            
        return graph
            
      
    def checkCycle(self,graph,source,visited,recstk):
        visited[source] = True
        recstk[source] = True 
        
        for v in graph[source]:
            if visited[v]==False and self.checkCycle(graph,v,visited,recstk):
                return True
            elif recstk[v] == True:
                return True
        recstk[source] = False
        return False