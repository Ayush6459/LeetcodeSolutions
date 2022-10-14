from sortedcontainers import SortedDict
class TimeMap :
    def __init__(self):
        self.map = {}

    def set(self, key:str, value : str , timeStamp:int) :
        if key not in self.map:
            self.map[key] = SortedDict()
        
        self.map[key][timeStamp] = value

    def get(self, key:str,timeStamp:int):
        if key not in self.map:return ""

        it = self.map[key].bisect_right(timeStamp)
        if it == 0:return ''
        return self.map[key].peekitem(it-1)[1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)