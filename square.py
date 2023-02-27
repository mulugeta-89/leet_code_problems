def square(nums):
    nums = list(map(lambda x: x**2, nums))
    return sorted(nums)