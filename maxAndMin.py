def maxandmin(arr):
    if len(arr) == 1:
        return arr[0]
    mid = len(arr)//2
    left_arr = arr[:mid]
    right_arr = arr[mid:]
    left_max = maxandmin(left_arr)
    right_max = maxandmin(right_arr)

    # return max(left_max, right_max)
    return min(left_max, right_max)
print(maxandmin([3,5,4,3,4,5,3,4,5,2]))