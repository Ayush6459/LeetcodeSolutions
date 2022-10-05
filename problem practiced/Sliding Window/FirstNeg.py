'''
Print first negative number in every window of size k from an array of size n.

Example : 
    arr = [12,-1,-7,8,- 15,30,16,18], k = 3
    output : [-1,-1,-7,-15,-15,0] # print 0 if no negative number is there in window of size k.

'''
# Function to print first negative number in every window of size k from an array of size n.
# Approach using extra array to store the negative numbers.
# Time Complexity: O(n)
# Space Complexity: O(n)
def printFirstNeg(arr, n, k):
    # Code here
    res = [] # to store the result
    neg = [] # to store the negative numbers

    i= 0 
    j =0
    while j<n:
        # if the current element is negative, add it to the neg list
        if arr[j]<0:
            neg.append(arr[j])
        # check if the window size is hit or not
        if j-i+1 < k:
            j+=1
            continue
        # if the window size is hits 
        # check for the first negative number in the window and add it to the result
        # if no negative number is there in the window, add 0 to the result
        elif j-i+1 == k:
            if len(neg)>0:
                res.append(neg[0])
                # if the arr[i] = neg[0], then we need to remove it from the neg list
                if arr[i] == neg[0]:
                    neg.pop(0)
                i=i+1
            else:
                res.append(0)
                i=i+1
        j+=1
    return res

# My approach of without using extra array
'''
    we can use a index variable to point at the index of negative number in the array.
    In worst case it time complexity is O(n^2)
    space complexity is O(1)
'''
def printFirstNeg1(arr, n, k):
    res = [] # to store the result
    i= 0
    j =0
    index = -1
    while j<n:
        # check if the current window size is hit or not
        # along with that we will track of the first negative number encouter 
        if j-i+1 < k:
            if index<0 and arr[j]<0:
                index = j
            j+=1
            continue # continue the loop
        # if the window size is hits
        elif j-i+1 == k:
            # check if the index is less then i then we have to find the first negative number in i to j
            if index<i:
                temp = -1
                for x in range(i,j+1):
                    if arr[x]<0:
                        temp = x
                        break
                # store the value in the result
                if temp<0:
                    res.append(0)
                else:
                    res.append(arr[temp])
                    index = temp
                i+=1
            else:
                res.append(arr[index])
                i+=1
        j+=1
    return res 



# Driver program to test above function
arr = [12,-1,-7,8,-15,30,16,18]
k = 3
n = len(arr)
print(printFirstNeg1(arr, n, k))

            
