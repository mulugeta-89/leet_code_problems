def searchInsert(arr, target):
    left = 0
    right = len(arr)-1
    while left <= right:
        mid = (left + right)/2
        mid = int(mid)
        if left == right:
            if arr[right] < target:
                return right + 1
            else:
                return right
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid-1
        else:
            left = mid + 1
    return mid
print(searchInsert([1,3], 0))
