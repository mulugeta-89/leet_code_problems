def prefixString(s, words):
    new_string = ""
    for i in range(len(words)):
        new_string = "".join(words[:i+1])
        if new_string == s:
            return True
    return False
print(prefixString("a", ["aa","aaaa","banana"]))