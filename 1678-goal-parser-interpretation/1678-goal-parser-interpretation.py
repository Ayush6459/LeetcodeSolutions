class Solution:
    def interpret(self, command: str) -> str:
        res = []
        i = 0
        while i<len(command):
            if command[i] =='(':
                if command[i+1] ==')':
                    res.append('o')
                    i+=2
                elif command[i+1] == 'a':
                    res.append('al')
                    i+=4
            else:
                res.append(command[i])
                i+=1
        return ''.join(res)