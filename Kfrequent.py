from collections import Counter
def frequent(nums, k):
    nums_dict = dict(Counter(nums))
    nums_dict = dict(sorted(nums_dict.items(), key=lambda item: item[1], reverse=True))
    result_key = list(nums_dict.keys())
    return result_key[:k]
    
print(frequent([1], 1))

