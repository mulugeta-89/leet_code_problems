def lengthOfLast(word):
    word2 = word.split(" ")
    word2.reverse()
    word3 = []
    for item in word2:
        if item == "":
            continue
        else:
            word3.append(item)
    print(word3)

print(lengthOfLast("what     you name   "))
