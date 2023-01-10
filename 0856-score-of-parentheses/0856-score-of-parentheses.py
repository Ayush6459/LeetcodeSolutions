class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        '''
        stk = [0]
        for i in s:
            if i == '(':
                stk.append(0)
            else:
                v = max(2*stk.pop(),1)
                stk[-1]+=v
                            
        return stk.pop() 
        TC :- O(N),  SC :- O(N)
        '''
        
        # optimised Solution
        ans = bal = 0
        for i, x in enumerate(S):
            if x == '(':
                bal += 1
            else:
                bal -= 1
                if S[i-1] == '(':
                    ans += 1 << bal
        return ans
        # TC : O(N) , SC : O(1)
    
    
    
    
    
    
    
    
    
    