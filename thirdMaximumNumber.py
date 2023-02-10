def thirdMaximumNumber(nums):
    new_arr = sorted(set(nums), reverse=True)
    if len(new_arr) < 2:
        return max(new_arr)
    return new_arr[2]
print(thirdMaximumNumber([3,2,1]))