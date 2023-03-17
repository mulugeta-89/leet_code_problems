def applyOperation(nums):
    for i in range(len(nums)-1):
        if nums[i] != nums[i+1]:
            continue
        else:
            nums[i] = nums[i]*2
            nums[i+1] = 0
    nums1 = nums.copy()
    left = 0
    right = len(nums1)-1
    for i in range(len(nums1)):
        if nums1[i]!= 0:
            nums[left] = nums1[i]
            left +=1
        if nums1[i]==0:
            nums[right] = nums1[i]
            right -=1
    return nums

print(applyOperation([1,2,2,1,1,0,3]))
