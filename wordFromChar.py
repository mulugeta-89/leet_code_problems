def countCharacters(words, chars):
    result = 0
    for word in words:
        for ch in word:
            if word.count(ch) > chars.count(ch):
                break
        else:
            result += len(word)   
    return result 
                
print(countCharacters(["cat", "bt", "hat", "tree"],"atach"))