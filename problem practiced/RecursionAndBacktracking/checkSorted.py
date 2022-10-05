def check(arr,n,i):
    if i == n-1 or not arr:
        return True 
    elif arr[i]<=arr[i+1] and i<n-1:
        return check(arr,n,i+1)
    else:
        return False

arr = []
print(check(arr,len(arr),0))
        