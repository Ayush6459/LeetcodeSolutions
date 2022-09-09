class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        def dfs(adj,currIndex,lastIndex,visited,res):
            if visited[-1]==lastIndex:
                res.append(visited)
                return 
            for v in adj[currIndex]:
                dfs(adj,v,lastIndex,visited+[v],res)
            return res
        
        
        
        #print(res)
        return dfs(graph,0,len(graph)-1,[0],[])
        