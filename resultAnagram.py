def result(words):
    words2 = words.copy()
    for i in range(1, len(words2)):
        if ''.join(sorted(words2[i-1])) == "".join(sorted(words2[i])):
            words.remove(words2[i])
    return words
print(result(["abba","baba","bbaa","cd","cd"]))