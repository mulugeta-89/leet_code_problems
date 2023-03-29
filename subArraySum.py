def subarray(nums, k):
    i,j = 0,1
    counter = 0
    while i<=len(nums) and j <= len(nums):
        running = nums[i:j]
        if sum(running) == k:
            counter += 1
        if j == len(nums):
            i += 1
            j = i
        j+=1
    return counter
print(subarray([1,1,1], 3))