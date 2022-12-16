class Solution:
    def isValid(self, s: str) -> bool:
        opcl = {'(': ')', '[': ']', '{': '}'}    #dict(('()', '[]', '{}'))
        stack = []
        openParan = {'(','{','['}
        for paran in s:
            if paran in openParan:
                stack.append(paran)
            elif len(stack) == 0 or paran != opcl[stack.pop()]:
                return False
        return len(stack) == 0