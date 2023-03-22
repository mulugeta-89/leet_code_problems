from collections import Counter
def lucky(arr):
    maxi = 0
    some_dict = Counter(arr)
    for key in some_dict.keys():
        if key == some_dict[key]:
            maxi = max(maxi, key)
    return maxi if maxi != 0 else -1
print(lucky([2,2,2,3,3]))