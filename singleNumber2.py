from collections import Counter
def singleNumber(nums):
    nums_dict = dict(Counter(nums))
    for key in nums_dict.keys():
        if nums_dict[key] == 1:
            return key