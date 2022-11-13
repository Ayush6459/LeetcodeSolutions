class Solution:
    def reverseWords(self, s: str) -> str:
        ans = []
        j = len(s)-1
        while j>=0:
            if s[j] == ' ':
                j-=1
            else:
                
                i=j
                while i>=0:
                    if s[i]==' ':
                        break
                    else:
                        i-=1
                ans.append(s[i+1:j+1])
                j=i
        return " ".join(ans)
        
            