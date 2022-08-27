class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        return self.solve(s,'',[],0)
    def solve(self,s:str,temp:str,ans:List[str],index:int):
        # base case 
        if index == len(s):
            ans.append(temp)
            return 
        if s[index].isdigit():
            self.solve(s,temp+s[index],ans,index+1)
        elif s[index].islower():
            self.solve(s,temp+s[index],ans,index+1)
            self.solve(s,temp+s[index].upper(),ans,index+1)
            
        elif s[index].isupper():
            self.solve(s,temp+s[index],ans,index+1)
            self.solve(s,temp+s[index].lower(),ans,index+1)
        
        return ans