def missing(arr,k):
    sol_arr = []
    for i in range(len(arr)+k):
        if i not in arr:
            sol_arr.append(i)
    return sol_arr[k]

print(missing([2,3,4,7,11],5))