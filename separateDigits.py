def separateDigits(nums):
    new_arr = []
    nums = list(map(lambda x: str(x), nums))
    for item in nums:
        item = list(item)
        for little in item:
            new_arr.append(little)
    return list(map(lambda x: int(x), new_arr))
print(separateDigits([13,25,83,77]))