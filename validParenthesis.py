def valid(letters):
    new_word = []
    for i in range(len(letters)):
        if letters[i] == "(":
            new_word.append(")")
        elif letters[i] == ("["):
            new_word.append("]")
        elif letters[i] == "{":
            new_word.append("}")
        elif new_word.pop() != letters[i]:
            return False
    return len(new_word) == 0
print(valid("{]"))

