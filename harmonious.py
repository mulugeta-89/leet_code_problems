from collections import Counter
def harmon(nums):
    nums_dict = dict(Counter(nums))
    nums_dict = dict(sorted(nums_dict.items(), key=lambda x: x[0]))
    keys = list(nums_dict.keys())
    new_arr = []
    for i in range(len(keys)-1):
        if keys[i] == keys[i+1]-1:
            new_arr.append(keys[i])
            new_arr.append(keys[i+1])
    if len(new_arr) == 0:
        return 0
    new_arr = list(set(new_arr))
    new_arr.sort()
    sol_arr = []
    for i in range(len(new_arr)-1):
        if new_arr[i] == new_arr[i+1]-1:
            maxi = nums_dict[new_arr[i]] + nums_dict[new_arr[i+1]]
            sol_arr.append(maxi)
    return max(sol_arr)

print(harmon([2,74,83,62,97,51,43,50,46,41,49,52,64,43,58,79,71,35,59,30,19,91,88,13,86,1,5,39,27,45,58,8,30,63,49,12,80,87,42,36,91,88,70,20,36,40,21,66,75,71,33,43,95,62,91,20,95,7,33,84,38,61,4,10,34,31,39,57,23,9,29,18,99,88,64,96,83,17,90,34,27,89,59]))
