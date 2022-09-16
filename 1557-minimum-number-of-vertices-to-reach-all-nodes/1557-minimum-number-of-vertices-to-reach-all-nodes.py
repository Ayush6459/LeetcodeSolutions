class Solution:
    def findSmallestSetOfVertices(self, n: int, A: List[List[int]]) -> List[int]:
        B = set(range(n))
        for x,y in A:
            if y in B:
                B.remove(y)
        return list(B)