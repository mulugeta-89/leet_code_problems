from collections import Counter
def sortArray(nums):
    nums_dict = (Counter(nums))
    nums_dict = dict(sorted(nums_dict.items(), key=lambda item: (item[1], -item[0])))
    sol_arr = []
    for key, value in nums_dict.items():
        for i in range(value):
            sol_arr.append(key)
    return sol_arr
print(sortArray([2,3,1,3,2]))