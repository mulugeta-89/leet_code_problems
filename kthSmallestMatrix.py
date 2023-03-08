def smallest(matrix,k):
    sol_arr = []
    for item in matrix:
        sol_arr +=item
    sol_arr.sort()
    return sol_arr[k-1]
print(smallest([[1,5,9],[10,11,13],[12,13,15]]))