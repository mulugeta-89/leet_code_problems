def binary(nums):
    low, high = 0, len(nums)-1
    nums_copy = nums.copy()
    nums.sort()
    while low < high:
        mid = (low + high) // 2
        if nums[mid] > nums[mid + 1]:
            high = mid
        else:
            low = mid + 1
    return nums_copy.index(nums[low])

    #alternative implementation
    left, right = 0, len(nums)
    while left < right:
        mid = (left+right)//2
        if nums[mid] > nums[mid+1]:
            right=mid
        else:
            left=mid+1
    return left
print(binary([6,5,4,3,2,3,2]))