def nextGreater(nums):
    nums1 = nums.copy()
    nums += nums1
    sol_arr = []
    flag = False
    for i in range(len(nums1)):
        for j in range(i+1, len(nums)):
            if nums[j] > nums1[i]:
                sol_arr.append(nums[j])
                flag = True
                break
        if not flag:
            sol_arr.append(-1)
        flag = False
    return sol_arr
print(nextGreater([1,2,3,4,3]))