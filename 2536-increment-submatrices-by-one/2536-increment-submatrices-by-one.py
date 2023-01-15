class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        v = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(len(queries)):
            for j in range(queries[i][0], queries[i][2]+1):
                v[j][queries[i][1]]+=1
                if 1+queries[i][3]!=n : v[j][queries[i][3]+1]-=1
                    
        print(v)
        for i in range(n):
            for j in range(1,n):
                v[i][j]+=v[i][j-1]
                
        return v
        