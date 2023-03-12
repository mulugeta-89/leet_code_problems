from collections import Counter
def sorting(nums):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] > nums[j]:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
    return nums
print(sorting([2,0,2,1,1,0]))

