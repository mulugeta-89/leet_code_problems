def anagram(s,p):
    sol_arr = []
    p_l = len(p)
    counter = 0
    for i in range(len(s)-len(p)+1):
        small = s[i:p_l+counter]
        if sorted(small) == sorted(p):
            sol_arr.append(counter)
        counter += 1
    return sol_arr
print(anagram("abab", "abcd"))
