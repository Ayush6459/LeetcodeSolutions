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

if __name__ == '__main__':
    
    uf = UnionFind(5)
    uf.Union(4,3)
    print(uf.parent)
    uf.Union(2,1)
    print(uf.parent)
    uf.Union(1,3)
    print(uf.parent)
    print(uf.rank)


