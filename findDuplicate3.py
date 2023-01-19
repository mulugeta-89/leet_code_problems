def duplicate(arr):
    new_arr = []
    for item in arr:
        item = abs(item)
        if arr[item-1] > 0:
            arr[item-1] = arr[item-1] *-1
        else:
            new_arr.append(item)
    return new_arr
print(duplicate([4,3,2,7,8,2,3,1]))
