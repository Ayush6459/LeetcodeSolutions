#User function Template for python3

class Solution:
    def inSequence(self, a, x, d):
        # code here
        if d == 0:
            return 1 if x == a else 0
     
    # Else difference between x
    # and a must be divisible by d.
        return 1 if ((x - a) % d == 0 and
                int((x - a) / d) >= 0) else 0
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        A, B, C = [int(x) for x in input().split()]
        
        ob = Solution();
        print(ob.inSequence(A, B, C))
# } Driver Code Ends