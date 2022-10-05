def LSWRC(s):
    i = 0
    j = 0
    length = len(s)
    s1 = set()
    res = 0

    while j<length:
        if s[j] not in s1:
            s1.add(s[j])
            j+=1
            continue
        else:
            res = max(res,len(s1))
            while s1 and s[j] in s1:
                s1.remove(s[i])
                i+=1

            s1.add(s[j])
            j+=1
            

    print(res)   


LSWRC('pwwkew')
