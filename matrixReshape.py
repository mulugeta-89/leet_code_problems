def matrixReshape(mat, r , c):
    a = len(mat[0])
    b = len(mat)
    sol_arr = []
    small_arr = []
    if a*b != r*c:
        return mat
    else:
        for i in range(len(mat)):
            for item in mat[i]:
                small_arr.append(item)
                if len(small_arr)==c:
                    sol_arr.append(small_arr)
                    small_arr = []
    return sol_arr
print(matrixReshape([[1,2],[5,6]],1,4))