class UnionFind:
    def __init__(self,N):
        self.parent = list(range(N))
        self.rank =  [0]*N

    def Find(self,a):
        if self.parent[a] != a:
            self.parent[a] = self.Find(self.parent[a])
        return self.parent[a]

    def Union(self,a,b):
        ra,rb = self.Find(a) , self.Find(b)
        if ra == rb : return 
        elif self.rank[ra] > self.rank[rb]:
            self.parent[rb] = ra 
        elif self.rank[rb]>self.rank[ra]:
            self.parent[ra] = rb
        else:
            self.parent[rb] = ra 
            self.rank[ra] +=1


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf  = UnionFind(len(edges))
        ans =[]
        for u,v in edges:
            if uf.Find(u-1) == uf.Find(v-1):
                ans = [u,v]
            else:
                uf.Union(u-1,v-1)
        return ans