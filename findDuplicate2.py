def duplicate(arr):
    new_arr = []
    for i in range(len(arr) - 1):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
            if min_idx != i:
                temp = arr[i]
                arr[i] = arr[min_idx]
                arr[min_idx] = temp
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            new_arr.append(arr[i])
    return new_arr
print(duplicate([4,3,2,7,8,2,3,1]))