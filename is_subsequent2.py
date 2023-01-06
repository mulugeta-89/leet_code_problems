def is_subsequent(s, t):
    if not s:
        return True
    if len(s) > len(t):
        return False
    sequence = 0
    for i in range(len(t)):
        if sequence <= len(s):
            if s[sequence] == t[i]:
                sequence += 1
    return sequence == len(s)
        
print(is_subsequent("abc", "abcd"))