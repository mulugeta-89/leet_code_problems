def findDifference(s,t):
    s = list(s)
    t = list(t)
    for item in t:
        if item not in s:
            return item
        else:
            s.pop(s.index(item))
print(findDifference("a","aa"))