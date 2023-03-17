def countPrefix(words, s):
    counter = 0
    for i in range(len(s)):
        new_string = s[:i+1]
        counter += words.count(new_string)
    return counter
print(countPrefix(["a","a"], "aa"))