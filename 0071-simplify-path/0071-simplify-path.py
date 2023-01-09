class Solution:
    def simplifyPath(self, path: str) -> str:
        a=[]
        cur=''
        for i in path + '/':
            if i=='/' :
                if cur == '..':
                    if a: a.pop()
                elif cur!='' and cur!='.':
                    a.append(cur)
                cur=''
            else:
                cur+=i
        return '/'+'/'.join(a)
