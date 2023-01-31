def moveZeros(nums):
    nums1 = nums.copy()
    left = 0
    right = len(nums1)-1
    for i in range(len(nums1)):
        if nums1[i]!=0:
            nums[left] = nums1[i]
            left+=1
        if nums1[i]==0:
            nums[right] = nums1[i]
            right -=1
print(moveZeros([0]))