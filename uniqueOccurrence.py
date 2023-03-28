from collections import Counter
def unique(arr):
    arr_dict = Counter(arr)
    return len(set(arr_dict.values())) == len(arr_dict.keys())
print(unique([-3,0,1,-3,1,1,1,-3,10,0]))
