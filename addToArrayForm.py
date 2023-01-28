def addArray(arr, num):
    arr2 = "".join(list(map(lambda x: str(x),arr)))
    return list(map(lambda x: int(x),list((str(int(arr2) + num)))))
print(addArray([1,2,3], 3))