def majorityElement(nums):
    nums_dict = {}
    for item in nums:
        if item not in nums_dict:
            nums_dict[item] = 1
        else:
            nums_dict[item] = nums_dict[item]+1
    print(nums_dict)
    for key in nums_dict.keys():
        if nums_dict[key] >= (len(nums)+1)/2:
            return key
print(majorityElement([2,2,1,1,1,2,2]))