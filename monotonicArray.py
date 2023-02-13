def monotonic(arr):
    a = sorted(arr)
    b = sorted(arr, reverse=True)
    if arr == a or arr == b:
        return True
    else:
        return False
print(monotonic([1,2,3,4,5]))