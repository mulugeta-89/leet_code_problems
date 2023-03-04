from collections import Counter

def intersection(nums):
    nums = list(map(lambda item: set(item), nums))
    new_arr = []
    for item in nums:
        for little in item:
            new_arr.append(little)
    arr_dict = dict(Counter(new_arr))
    sol_arr = []
    for key in arr_dict.keys():
        if arr_dict[key] == len(nums):
            sol_arr.append(key)
    return sorted(sol_arr)

    
print(intersection([[7,34,45,10,12,27,13],[27,21,45,10,12,13]]))