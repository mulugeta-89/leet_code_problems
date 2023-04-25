from collections import Counter

def replacing(nums, operations):
    nums_dict = {num: i for i, num in enumerate(nums)}
    for s, e in operations:
        i = nums_dict[s]
        nums[i] = e
        nums_dict[e] = i
        del nums_dict[s]
    return nums
print(replacing([1,2],[[1,3],[2,1],[3,2]]))