def decodedString(s,k):
    r = ""
    for item in s:
        if item.isalpha():
            r += item
            if len(r) == k:
                return r[k-1]
        if item.isdigit():
            repeat = int(item)
            if len(r) * repeat == k:
                return r[(k-1)]
            r *= repeat

    #alternative
    r = ""
    for item in s:
        if item.isalpha():
            r += item
        if item.isdigit():
            r += r*(int(item)-1)
    return r[k-1]
print(decodedString("leet2code3",10))