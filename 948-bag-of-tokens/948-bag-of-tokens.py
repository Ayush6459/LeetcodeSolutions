class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        if not tokens or power<tokens[0]  :
            return 0
        s = 0
        i,j=0,len(tokens)-1
        while i<=j:
            if tokens[i]<=power:
                power-=tokens[i]
                s+=1
                i+=1
            else:
                if i==j:
                    break
                else:
                    power+=tokens[j]
                    s-=1
                    j-=1
        return s
    