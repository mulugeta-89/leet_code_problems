from collections import Counter
def removeDup(nums):
    nums_dict = Counter(nums)
    nums.clear()
    for key in nums_dict.keys():
        if nums_dict[key] >= 2:
            for i in range(2):
                nums.append(key)
        else:
            nums.append(key)
    return len(nums)
print(removeDup([0,0,1,1,1,1,2,3,3]))