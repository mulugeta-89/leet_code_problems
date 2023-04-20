def reverseg(word,ch):
    word = list(word)
    inde = word.index(ch)
    that_word = word[:inde+1]
    that_word = that_word[::-1]
    for i in range(inde+1):
        word[i] = that_word[i]
    return "".join(word)
print(reverseg("abcdefd", "d"))
