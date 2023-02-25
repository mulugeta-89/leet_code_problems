def findLength(a,b):
    if a==b:
        return -1
    else:
        return max(len(a), len(b))
         
print(findLength("aa", "aaa"))