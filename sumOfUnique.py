def sum(nums):
    nums_dict = Counter(nums)
    total = 0
    for key in nums_dict.keys():
        if nums_dict[key] == 1:
            total += key
    return total