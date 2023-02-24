def sortArray(nums):
    other_nums = nums.copy()
    sol_arr = []
    even = 0
    odd = 1
    for i in range(len(nums)):
        if nums[i] %2 == 0:
            other_nums[even] = nums[i]
            even += 2
        else:
            other_nums[odd] = nums[i]
            odd += 2
    return other_nums
print(sortArray([4,2,5,7]))
        


