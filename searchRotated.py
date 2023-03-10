def search(nums, target):
    if target in nums:
        return nums.index(target)
    return -1