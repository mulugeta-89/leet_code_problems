def repeatedSubstring(s):
    for i in range(len(s)//2):
        little_string = s[:i+1]
        len_little = len(little_string)
        multiple = len(s)//len_little
        if little_string*multiple==s:
            return True
    return False

print(repeatedSubstring("abcabc"))
