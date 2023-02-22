def construct2DArray(original, m,n):
    sol_arr = []
    small_arr = []
    if len(original) != m*n:
        return []
    else:
        for item in original:
            small_arr.append(item)
            if len(small_arr) == n:
                sol_arr.append(small_arr)
                small_arr = []
    return sol_arr
print(construct2DArray([1,2,3,4],1,4))
