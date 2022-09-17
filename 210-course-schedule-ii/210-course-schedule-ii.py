class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = self.makeGraph(prerequisites,numCourses)
        visited = [False]*numCourses
        recstk = [False]*numCourses
        res = []
        #print(graph)
        for i in range(numCourses):
            if visited[i]==False:
                if self.checkCycle(graph,i,visited,recstk,res):
                    return []
                
        return res
        
    def makeGraph(self,edges,vertex):
        graph = [[] for i in range(vertex)]
        for x,y in edges:
            graph[y].append(x)
            
        return graph
            
      
    def checkCycle(self,graph,source,visited,recstk,res):
        visited[source] = True
        recstk[source] = True 
        
        for v in graph[source]:
            if visited[v]==False and self.checkCycle(graph,v,visited,recstk,res):
                return True
            elif recstk[v] == True:
                return True
        recstk[source] = False
        res.insert(0,source)
        return False