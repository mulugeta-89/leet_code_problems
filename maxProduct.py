def maxProduct(nums):
    nums = list(map(lambda item: item-1, nums))
    nums = sorted(nums, reverse=True)
    return nums[0]*nums[1]
print(maxProduct([3,4,5,2]))