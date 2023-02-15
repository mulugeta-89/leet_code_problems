
def keyboardRow(arr):
    word1 = set("qwertyuiop")
    word2 = set("asdfghjkl")
    word3 = set("zxcvbnm")
    new_arr2 = []
    for item in arr:
        item2 = set(item.lower())
        if item2 <= word1 or item2 <= word2 or item2 <= word3:
            new_arr2.append(item)
    return new_arr2
        

print(keyboardRow(["Hello","Alaska","Dad","Peace"]))