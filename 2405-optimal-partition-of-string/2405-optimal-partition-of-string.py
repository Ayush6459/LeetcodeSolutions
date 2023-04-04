class Solution:
    def partitionString(self, s: str) -> int:
        res = []
        i = 0
        while i<len(s):
            temp = set()
            while i<len(s) and s[i] not in temp :
                temp.add(s[i])
                i+=1
            res.append(''.join(temp))
            
        return len(res)