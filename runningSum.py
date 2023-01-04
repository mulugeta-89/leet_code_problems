def runingSum(nums):
    runSums = []
    total = 0
    for i in range(len(nums)):
        total +=  nums[i]
        runSums.append(total)
    return runSums
print(runingSum([1,2,3]))