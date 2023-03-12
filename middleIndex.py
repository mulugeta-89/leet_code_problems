def middle(nums):
    for i in range(len(nums)):
        if i==0:
            left_sum =0
        if i == len(nums)-1:
            right_sum = 0
        left_sum = sum(nums[:i])
        right_sum = sum(nums[i+1:])
        if left_sum == right_sum:
            return i
    return -1
print(middle([2,3,-1,8,4]))