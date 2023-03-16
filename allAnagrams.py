def anagrams(s, p):
    matrix = []
    sol_arr = []
    p_l = len(p)
    counter = 0
    for i in range(len(s)-len(p)+1):
        matrix.append(s[i:p_l+counter])
        counter += 1
    for item in matrix:
        if sorted(item) == sorted(p):
            sol_arr.append(matrix.index(item))
            matrix[matrix.index(item)] = ""
    return sol_arr
print(anagrams("cbaebabacd", "abc"))