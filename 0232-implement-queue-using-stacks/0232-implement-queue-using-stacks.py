class MyQueue(object):

    def __init__(self):
        self.li=[]

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.li.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        
        pop_ele = self.li[0]
        self.li = self.li[1:]
        return(pop_ele)
        

    def peek(self):
        """
        :rtype: int
        """
        return(self.li[0])
        

    def empty(self):
        """
        :rtype: bool
        """
        if len(self.li) == 0:
            return True
        else:
            return False  
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()