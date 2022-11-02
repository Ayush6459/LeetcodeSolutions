from queue import Queue 
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank = set(bank)
        if end not in bank:
            return -1
        queue = Queue()
        queue.put((start,0))
        visited = {start}
        while not queue.empty():
            gene , level = queue.get()
            if gene == end:
                return level
            for i in range(len(gene)):
                for letter in 'ACGT':
                    new_gene = gene[:i] + letter + gene[i+1:]
                    if new_gene not in visited and new_gene in bank:
                        queue.put((new_gene,level+1))
                        visited.add(new_gene)
        return -1
        