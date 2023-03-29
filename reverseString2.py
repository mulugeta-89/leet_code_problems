def reverseString(s, k):
    new_str = []
    for i in range(0,len(s), 2*k):
        some_arr = s[i:i+k]
        other_arr = s[i+k:i+(2*k)]
        new_str += some_arr[::-1]
        new_str += other_arr
    return new_str
print(reverseString("abcd", 2))
        
        
