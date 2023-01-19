def removeDuplicate(arr):
    arr_dict = {}
    for item in arr:
        if item not in arr_dict:
            arr_dict[item] = 1
        else:
            continue
    return len(list(arr_dict.keys()))
print(removeDuplicate([0,0,1,1,1,2,2,3,3,4]))