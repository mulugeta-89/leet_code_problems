def intersection(arr1, arr2):
    new_arr = []
    for item in arr1:
        while item in arr2:
            arr2.pop(arr2.index(item))
            new_arr.append(item)
            break
    return new_arr


print(intersection([1,2,2,1],[2]))