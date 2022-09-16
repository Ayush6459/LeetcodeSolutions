class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        incoming = [0]*n
        for i in edges:
            incoming[i[1]]+=1
        res = []
        for i in range(n):
            if incoming[i] ==0:
                res.append(i)
        return res