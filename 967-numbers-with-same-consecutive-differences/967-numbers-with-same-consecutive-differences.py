class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        def generate(s,n,k,res):
            if len(s)==n:
                res.append(int(s))
                return 
            x = int(s[-1])
            if k == 0:
                generate(s+str(x),n,k,res)
            else:
                if x-k >=0:
                    generate(s+str(x-k),n,k,res)
                if x+k<=9:
                    generate(s+str(x+k),n,k,res)
            return res 
        
        result = []
        s = '1'
        while int(s)<=9:
            temp = generate(s,n,k,[])
            result.extend(temp)
            s=str(int(s)+1)
            
        return result