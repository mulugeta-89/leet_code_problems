def search(matrix, target):
    new_arr = []
    for item in matrix:
        new_arr += item
    left = 0
    right = len(new_arr)-1
    while left <= right:
        mid = (left+right)//2
        if new_arr[mid] == target:
            return True
        elif new_arr[mid] > target:
            right = mid-1
        else:
            left = mid+1
    return False
print(search([[1,3,5,7],[10,11,16,20],[23,30,34,60]],3))