class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        freq = collections.Counter(s)
        return False if len(set(freq.values()))>1 else True