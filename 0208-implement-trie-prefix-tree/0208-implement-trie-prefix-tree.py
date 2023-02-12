class Trie:

    def __init__(self):
        self.Char_Size = 26
        self.isLeaf = False
        self.children = [None]*self.Char_Size
    def insert(self, key: str) -> None:
        root = self
        for i in range(len(key)):
            idx = ord(key[i])-ord('a')
            if root.children[idx] is None:
                root.children[idx] = Trie()
            root = root.children[idx]
        root.isLeaf = True

    def search(self, word: str) -> bool:
        root = self
        for i in range(len(word)):
            idx = ord(word[i]) - ord('a')
            if root.children[idx] is None : return False
            root = root.children[idx]
        return root.isLeaf

    def startsWith(self, prefix: str) -> bool:
        root = self
        for i in range(len(prefix)):
            idx = ord(prefix[i]) - ord('a')
            if root.children[idx] is None : return False
            root = root.children[idx]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)