class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stk = [0]
        for i in s:
            if i == '(':
                stk.append(0)
            else:
                v = max(2*stk.pop(),1)
                stk[-1]+=v
                            
        return stk.pop()