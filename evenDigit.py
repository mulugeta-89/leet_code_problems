def evenDigit(nums):
    sol_arr = []
    nums = list(map(lambda x: str(x), nums))
    for item in nums:
        counter = 0
        for little in item:
            counter += 1
        sol_arr.append(counter)
    counter = 0
    for item in sol_arr:
        if item %2 == 0:
            counter += 1
    return counter
print(evenDigit([12,345,2,6,7896]))