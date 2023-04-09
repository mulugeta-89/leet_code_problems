def single(nums):
    nums_dict = Counter(nums)
    nums_dict = dict(sorted(nums_dict.items(), key=lambda x: x[1]))
    for key in nums_dict:
        return key
