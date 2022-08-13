class Solution:
    def findAnagrams(self, s1: str, s2: str) -> List[int]:
        '''
            solution :
                we will use the sliding window approach to find the anagrams.
                Since we have to find the string s2 in s1 so our window size will be equal to the                     length of s2.
                we will use the hashmap to store the count of each character in the window.
                if the count of the character in the window is equal to the count of the character in                 s2 then we will add the start index in result list
                else just slide the window and continue

        '''
        
        k = len(s2) # to store the window size 
        res = [] # to store the result
        # store the count of each character in the s2
        dic = {}
        for i in s2:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1

        count = len(dic) # to store the count of distinct characters in the s2
        # so the idea is that we decrement the count by one if any of the value become zero in dictionary
        # using this concept we do not have to traverse the map again and again
        i,j = 0,0
        while j<len(s1):
            # calculation part 
            if s1[j] in dic:
                dic[s1[j]]-=1
                if dic[s1[j]]==0:
                    count-=1
            # check if the window size hit or not 
            if j-i+1 < k: # if the window size is not hit
                j+=1
                continue
            if j-i+1 == k: # if the window size is hit
                if count==0: # if the count is zero then we have found the anagram
                    res.append(i) # store the index in result
                    #print(s1[i],i)
                if s1[i] in dic:
                    dic[s1[i]]+=1
                    if dic[s1[i]]==1: # we will check if the transition happens here
                        count+=1

                # slide the window
                i+=1
                j+=1

        # return the result
        return res