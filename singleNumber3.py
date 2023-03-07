from collections import Counter
def singleNumber(nums):
    nums_dict = dict(Counter(nums))
    nums.clear()
    for key in nums_dict.keys():
        if nums_dict[key] == 1:
            nums.append(key)
    return nums