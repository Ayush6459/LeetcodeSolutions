


def LSOSK(arr,k):
    i=0
    j=0
    length = len(arr)
    cursum = 0
    res = -1
    while j<length:
        cursum+=arr[j]
        if cursum<k:
            j+=1
        elif cursum==k:
            #print(arr[i:j+1])
            res = max(res,j-i+1)
            j+=1
        else:
            
            while cursum>k:
                cursum-=arr[i]
                i+=1
            j+=1
        
    return res

print(LSOSK([4,1,1,1,2,3,5],5))