def arrayPartition(nums):
    sum = 0
    nums.sort()
    for i in range(0, len(nums), 2):
        sum += nums[i]
    return sum
print(arrayPartition([5,4,3,2,1]))