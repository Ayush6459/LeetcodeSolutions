from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs1 = [''.join(sorted(i)) for i in strs]
        d = {}
        for x,y in zip(strs,strs1):
            if y not in d:
                d[y] = [x]
            else:
                d[y].append(x)
        #print(d)
        
        return d.values()