def isArith(nums):
    flag = False
    for i in range(1,len(nums)):
        if nums[i] - nums[i-1] == nums[1] - nums[0]:
            flag = True
        else:
            return False
    return flag
def checkArtithmeticArray(nums, l, r):
    sol_arr = []
    for i in range(len(l)):
        new_arr = nums[l[i]:r[i]+1]
        new_arr.sort()
        result = isArith(new_arr)
        sol_arr.append(result)
        new_arr = []
    return sol_arr
print(checkArtithmeticArray([-12,-9,-3,-12,-6,15,20,-25,-20,-15,-10],[0,1,6,4,8,7], [4,4,9,7,9,10]))


