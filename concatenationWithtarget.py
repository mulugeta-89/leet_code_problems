def concatenation(nums, target):
    counter = 0
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i == j:
                continue
            running = nums[i] + nums[j]
            if running == target:
                counter += 1
    return counter
print(concatenation(["777","7","77","77"], "7777"))
