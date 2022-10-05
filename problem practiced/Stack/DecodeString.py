from curses.ascii import isalpha, isdigit


def decode(s:str)->str:

    i = 0
    s1 = [] # stack 1
    s2 = [] # stack 2

    while i<len(s):
        if s[i].isdigit():
            temp = s[i]
            i+=1
            while s[i].isdigit():
                temp = temp+s[i]
                i+=1
            s1.append(int(temp))
            i-=1
            
            #continue
        if s[i].isalpha() or s[i] =='[':
            s2.append(s[i])
            
            #continue
        if s[i] == ']':
            temp = ''
            while s2 and s2[-1]!='[':
                temp = s2.pop()+temp

            s2.pop()
            if s1:

                s2.append(temp*s1.pop())
            else:
                s2.append(temp)

        i+=1
            
            #continue
    temp = ''
    while s2:
        temp = s2.pop()+temp
    return temp


s = "100[leetcode]"
s1 = "3[a2[c]]"
y =decode(s)
x = len(y)
print(x)
print(y)

