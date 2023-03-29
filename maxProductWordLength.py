def intersection(s, j):
    flag = False
    for item in s:
        if item in j:
            flag = True
    return flag



def maxProduct(words):
    maxi = 0
    for i in range(len(words)-1):
        for j in range(i+1, len(words)):
            c = intersection(words[i], words[j])
            if not c:
                a = len(words[i])
                b = len(words[j])
                maxi = max(maxi, a*b)

    return maxi 
print(maxProduct(["a","aa","aaa","aaaa"]))