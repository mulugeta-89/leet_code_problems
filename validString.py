def validity(s):
    while("abc" in s):
        s = s.replace("abc","")
    return s == ""