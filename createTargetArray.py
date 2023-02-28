def targetArray(nums, index):
    sol_arr = []
    counter = 0
    for item in nums:
        sol_arr.insert(index[counter], item)
        counter += 1
    return sol_arr
print(targetArray([1,2,3,4,0],[0,1,2,3,0]))