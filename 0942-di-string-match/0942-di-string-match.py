class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        low = 0
        high = len(s)
        perm = []
        for i in range(high):
            if s[i] == 'I':
                perm.append(low)
                low+=1
            else:
                perm.append(high)
                high-=1
        perm.append(high)
        return perm