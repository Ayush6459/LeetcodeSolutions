#User function Template for python3


class Solution:
    def maxLength(self,arr,N):
        # Stores the length of current
        # subarray with positive product
        Pos = 0
     
        # Stores the length of current
        # subarray with negative product
        Neg = 0
     
        # Stores the length of the longest
        # subarray with positive product
        res = 0
     
        for i in range(N):
            if (arr[i] == 0):
     
                # Reset the value
                Pos = Neg = 0
     
            # If current element is positive
            elif (arr[i] > 0):
     
                # Increment the length of
                # subarray with positive product
                Pos += 1
     
                # If at least one element is
                # present in the subarray with
                # negative product
                if (Neg != 0):
                    Neg += 1
     
                # Update res
                res = max(res, Pos)
     
            # If current element is negative
            else:
                Pos, Neg = Neg, Pos
     
                # Increment the length of subarray
                # with negative product
                Neg += 1
     
                # If at least one element is present
                # in the subarray with positive product
                if (Pos != 0):
                    Pos += 1
     
                # Update res
                res = max(res, Pos)
                 
        return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():
        T=int(input())
        while(T>0):
            
            n=int(input())

            arr=[int(x) for x in input().strip().split()]
            
            
            obj = Solution()
            print(obj.maxLength(arr,n))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends