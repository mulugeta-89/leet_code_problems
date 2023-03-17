def counting(nums, k):
    sol = 0
    left = 0
    right = len(nums)-1

    while left < right:
        if abs(nums[left]-nums[right]) == k:
            sol += 1
        right -= 1
        if left == right:
            left += 1
            right = len(nums)-1
    return sol
print(counting([3,2,1,5,4],2))

        