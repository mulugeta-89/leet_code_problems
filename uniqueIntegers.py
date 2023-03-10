from collections import Counter
def uniqueInteger(arr,k):
    arr_dict = dict(Counter(arr))
    arr = sorted(arr, key=lambda x: (arr_dict[x], x))
    print(arr)
print(uniqueInteger([4,3,1,1,3,3,2],3))
