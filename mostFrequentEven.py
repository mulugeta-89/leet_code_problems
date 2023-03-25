from collections import Counter

def frequent(nums):
    nums = list(filter(lambda x: x%2==0, nums))
    nums_dict = Counter(nums)
    nums_dict = dict(sorted(nums_dict.items(), key=lambda x: (x[1],-x[0]), reverse=True))
    print(nums_dict)
    keys = list(nums_dict.keys())
    return keys[0] if keys else -1

print(frequent([8154,9139,8194,3346,5450,9190,133,8239,4606,8671,8412,6290]))