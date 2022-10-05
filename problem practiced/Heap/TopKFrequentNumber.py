import heapq 
'''
def check(arr):
    heapq.heapify(arr)
    return arr 

arr = [[5,1],[3,1],[1,3],[2,2],[4,1]]

print(check(arr))

'''

'''
Given an array find the top k frequent numbers
I/p : arr = [1,2,1,1,3,2,3,4] , k=2
O/p : [1,2]
'''
# using heap
def TopK(arr,k):
    # build the fequency map 
    freq = dict()
    for i in arr:
        if i not in freq:
            freq[i] = 1
        else:
            freq[i]+=1
    hp =[]
    heapq.heapify(hp)
    for i in freq:
        heapq.heappush(hp,[freq[i],i])
        if len(hp)>k:
            heapq.heappop(hp)

    return [i[1] for i in hp]
    
# using bucket sort concept
#
def TopK1(arr,k):
    # build the fequency map
    freq = dict()
    for i in arr:
        if i not in freq:
            freq[i] = 1
        else:
            freq[i] += 1

    bucket  = []





arr = [1,1,1,2,2,3]
k =2
hp =TopK(arr,k)
print(hp)

