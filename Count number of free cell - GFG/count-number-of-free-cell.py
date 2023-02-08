#User function Template for python3

class Solution():
    def countZero(self, n, k ,arr):
        #your code here
        N = n*n 
        RC = set()
        CC = set()
        res = []
        for r,c in arr:
            RC.add(r)
            CC.add(c)
            temp = len(RC)*n
            temp1= len(CC)*(n-len(RC))
            res.append(N-temp-temp1)
        
        return res
         

#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(int(input())):
    n,k=map(int,input().split())
    arr = []
    for i in range(k):
        x,y=map(int,input().split())
        arr.append([x, y])
    obj = Solution()
    res = obj.countZero(n, k, arr)
    for i in res:
        print(i,end = " ")
    print()
# } Driver Code Ends