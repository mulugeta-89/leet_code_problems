def binary(arr):

    left, right = 0, len(arr)
    while left < right:
        mid = (left+right)//2
        if arr[mid] > arr[mid+1]:
            right=mid
        else:
            left=mid+1
    return left