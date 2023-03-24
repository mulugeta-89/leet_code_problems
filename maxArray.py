from collections import Counter

def maxArray(nums):
    nums_dict = Counter(nums)
    counter = 0
    for key in nums_dict.keys():
        while(nums_dict[key] >= 2):
            nums_dict[key] -= 2
            counter += 1
            if nums_dict[key] <= 1:
                break
    other = 0
    print(nums_dict)
    for key in nums_dict.keys():
        if nums_dict[key] == 1:
            other += 1
    return [counter, other]


print(maxArray([0]))

