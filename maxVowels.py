def maxVowels(s,k):
    count = 0
    maxi = 0
    for i in range(k,len(s)+1):
        some = s[count:i]
        vowels = 0
        for item in some:
            if item == "a" or item == "e" or item == "i" or item == "o" or item == "u":
                vowels += 1
        maxi = max(maxi, vowels)
        count += 1
    return maxi

    #alternative

    count = 0
    maxi = 0
    for i in range(k,len(s)+1):
        vowels=0
        for j in range(count, i):
            if s[j] == "a" or s[j] == "e" or s[j] == "i" or s[j] == "o" or s[j] == "u":
                vowels += 1
        maxi = max(maxi, vowels)
        count += 1
    return maxi

    #alternative

    count = 0
    maxi = 0
    z = {"a","e","i","o","u"}
    for i, x in enumerate(s):
        if x in z:
            count += 1
        if i >=k and s[i-k] in z:
            count -= 1
        maxi = max(maxi, count)
    return maxi
        
print(maxVowels("abciiidef",3))