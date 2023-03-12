def summation(nums):
    sol_arr = []
    for i in range(len(nums)):
        if i==0:
            left_sum =0
        if i == len(nums)-1:
            right_sum = 0
        left_sum = sum(nums[:i])
        right_sum = sum(nums[i+1:])
        sol_arr.append(abs(left_sum-right_sum))
    return sol_arr
print(summation([10,4,8,3]))
    