def singleNumber(arr):
    arr_dict = {}
    for item in arr:
        if item not in arr_dict:
            arr_dict[item] = 1
        else:
            arr_dict[item] = arr_dict[item] + 1
    for item in arr_dict.keys():
        if arr_dict[item] == 1:
            return item
print(singleNumber([4,1,2,1,2]))
