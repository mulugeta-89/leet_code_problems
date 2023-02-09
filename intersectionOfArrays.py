def intersection(arr1, arr2):
    new_arr = []
    for i in range(len(arr1)):
        if arr1[i] in arr2:
            new_arr.append(arr1[i])
    return set(new_arr)


print(intersection([4,9,5],[9,4,9,8,4]))