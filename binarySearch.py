def binarySearch(num, target):
    left = 0
    right = len(num) -1
    while(left <= right):
        mid = (left + right) /2
        mid = int(mid)
        if num[mid] == target:
            return mid
        elif num[mid] > target:
            right = mid - 1
        elif num[mid] < target:
            left = mid + 1
    return -1
print(binarySearch([1,2,3,4,5,6,7], 1))
