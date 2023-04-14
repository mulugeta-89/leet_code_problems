def validTriangle(nums):
    nums.sort()
    count = 0
    for i in range(2, len(nums)):
        left, right = 0, i-1
        while left < right:
            if nums[left] + nums[right] > nums[i]:
                count += (right-left)
                right -= 1
            else:
                left += 1
    return count
    #optional
    nums.sort()
    count = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                if nums[i] + nums[j] > nums[k]:
                    count += 1
    return count
print(validTriangle([7,0,0,0]))
