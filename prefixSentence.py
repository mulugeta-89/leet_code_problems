def prefix_word(sentence, seachWord):
    arr = sentence.split(" ")
    len_word = len(seachWord)
    for item in arr:
        new_string = item[:len_word]
        if new_string == seachWord:
            return arr.index(item)+1
    return -1
print(prefix_word("this problem is an easy problem", "pro"))