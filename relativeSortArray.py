def relativeSortArray(arr1, arr2):
    new_arr = []
    other_arr = []
    for item in arr2:
        for item2 in arr1:
            if item2 == item:
                new_arr.append(item2)
    for item in arr1:
        if item not in new_arr:
            other_arr.append(item)
    return new_arr+sorted(other_arr)
print(relativeSortArray([28,6,22,8,44,17],[22,28,8,6]))