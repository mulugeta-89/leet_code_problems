def mergeSortedArray(arr1, arr2):
    for item in arr2:
        indexOfZero = arr1.index(0)
        arr1[indexOfZero] = item
    return arr1
