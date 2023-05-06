def num_sum(nums, target):
    nums.sort()
    left = 0
    total = 0
    mod = pow(10,7) + 7
    right = len(nums)-1
    while left <= right:
        if nums[left] + nums[right] > target:
            right -= 1
        else:
            total += pow(2, right-left)
            total %= mod
            left += 1
    return total
print(num_sum([2,3,3,4,6,7],12))

