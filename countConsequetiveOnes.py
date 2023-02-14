def countOnes(nums):
    counter = 0
    new_arr = []
    for item in nums:
        if item == 1:
            counter += 1
            new_arr.append(counter)
        else:
            counter = 0
    return 0 if len(new_arr) == 0 else max(new_arr)