def generate(s,n,k,res):
    if len(s)==n:
        res.append(int(s))
        return 
    x = int(s[-1])
    if x-k >=0:
        generate(s+str(x-k),n,k,res)
    if x+k<=9:
        generate(s+str(x+k),n,k,res)
    return res 


def solve(n,k):
    res = []
    s = '1'
    while int(s) <=9:
        temp = generate(s,n,k,[])
        res.extend(temp)
        s=str(int(s)+1)

    return res 

print(solve(2,1))
