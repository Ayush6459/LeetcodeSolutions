class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        def isConsistent(s,allowedset):
            
            for i in s:
                if i not in allowedset:
                    return False
            return True
        count = 0
        for i in words:
            if isConsistent(set(i),allowed):
                count+=1
        return count