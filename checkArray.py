def formArray(arr, pieces):
    sol_arr = []
    for i in range(len(arr)):
        for j in range(len(pieces)):
            if arr[i] == pieces[j][0]:
                sol_arr += pieces[j]
    return sol_arr == arr
print(formArray([49,18,16], [[16,18,49]]))