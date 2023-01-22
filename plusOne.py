def plusOne(arr):
    i = len(arr)-1
    while(i >= 0):
        if arr[i] < 9:
            arr[i] = arr[i] + 1
            return arr
        arr[i] = 0
        i = i -1
    if arr[0] == 0:
        arr.insert(0, 1)
    return arr

print(plusOne([9,9,2,3,4,9]))