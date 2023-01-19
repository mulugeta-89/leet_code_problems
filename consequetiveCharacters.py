def consequetive(word):
    count = 1
    new_arr = []
    prev = word[0]
    for i in range(1,len(word)):
        if word[i] == prev:
            count +=1
            new_arr.append(count)
        else:
            count = 1
            prev = word[i]
    if not new_arr:
        return 1
    else:
        return max(new_arr)
print(consequetive("tourist"))

