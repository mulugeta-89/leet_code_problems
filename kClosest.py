def closest(arr, k, x):
    arr.sort(key=lambda y: (abs(y-x)))
    return sorted(arr[:k])
print(closest([1,2,3,4,5],4,3))