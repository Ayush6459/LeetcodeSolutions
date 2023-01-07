class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        j = 0
        i = 1
        res = []
        while j<len(target) and i<=n:
            res.append("Push")
            if target[j] != i:
                res.append("Pop")
                i+=1
            else:
                j+=1
                i+=1
        return res
            