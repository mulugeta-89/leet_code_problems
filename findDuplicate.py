def duplicates(arr):
    arr_dict = {}
    new_arr = []
    for item in arr:
        if item not in arr_dict:
            arr_dict[item] = 1
        else:
            arr_dict[item]  = arr_dict[item] + 1
    #return arr_dict
    for item in arr_dict:
        if arr_dict[item] == 2:
            new_arr.append(item)
    return new_arr
print(duplicates([1,2,3,4,2,4]))
