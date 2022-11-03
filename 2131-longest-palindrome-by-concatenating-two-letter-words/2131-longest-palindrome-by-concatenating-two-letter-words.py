class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        freq = Counter(words)
        ans = 0
        haveCentral = False
        
        for word,count in freq.items():
            # if the word is palindrom
            if word == word[::-1]:
                # check if it is central element or not
                # if the word count is odd then it is a central element
                if count%2 == 0:
                    ans+=count
                else:
                    ans+=count - 1
                    haveCentral = True
            elif word[0]<word[1]: # this was done to choose only one element of non palindromic words pair 
                ans+= 2*min(count,freq[word[::-1]])
                
        if haveCentral:
            ans+=1
        return 2*ans
            