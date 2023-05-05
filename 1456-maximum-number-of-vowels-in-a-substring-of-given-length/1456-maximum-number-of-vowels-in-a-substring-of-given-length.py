class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = {'a','e','i','o','u'}
        n = len(s)
        q = deque()
        i = 0
        res = VC = 0
        while i<n:
            if len(q)<k:
                q.append(s[i])
                if s[i] in vowel : VC+=1
                res = max(res,VC)
                i+=1
            else:
                x = q.popleft()
                if x in vowel: VC-=1
                q.append(s[i])
                
                if s[i] in vowel : VC+=1
                res = max(res,VC)
                i+=1
        return res
        
        # TC : O(N) , SC : O(N)
                
        