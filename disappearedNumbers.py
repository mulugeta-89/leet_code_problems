def disppearedNumbers(arr):
    for i in range(len(arr)):
        index = abs(arr[i])-1
        if arr[index] > 0:
            arr[index]*= -1
    new_arr = []
    for i in range(len(arr)):
        if arr[i] > 0:
            new_arr.append(i+1)
    return new_arr


print(disppearedNumbers([1,1]))
