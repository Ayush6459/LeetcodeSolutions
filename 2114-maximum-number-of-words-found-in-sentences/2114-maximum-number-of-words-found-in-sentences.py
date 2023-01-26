class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        m =0
        for i in sentences:
            m = max(m,len(i.split()))
        return m