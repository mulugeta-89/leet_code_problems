from collections import Counter
def majority(nums):
    nums_dict = Counter(nums)
    sol_arr = []
    for item in nums_dict.keys():
        if nums_dict[item] > len(nums)//3:
            sol_arr.append(item)
    return sol_arr
print(majority([1]))
