from collections import Counter

def lonelies(nums):
    nums_dict = Counter(nums)
    # nums_dict = {k:v for k,v in nums_dict.items() if nums_dict[k] == 1}
    new_num = []
    for key in nums_dict:
        if nums_dict[key] > 1 or key +1 in nums or key-1  in nums:
            continue
        else:
            new_num.append(key)
    return new_num
            
print(lonelies([10,6,5,8]))
