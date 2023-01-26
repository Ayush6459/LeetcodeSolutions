class Solution:
    def longestWord(self, words: List[str]) -> str:
        # sort the words
        words.sort()
        hashtable = set(words)
        res = ['',0]
        def check(string):
            temp = ''
            for i in string:
                temp+=i
                if temp not in hashtable:
                    return False
            return True
        for i in words:
            if check(i):
                if res[1]<len(i):
                    res[0]= i
                    res[1] = len(i)
        return res[0]