def largest(nums, k):
    nums = sorted(nums, reverse=True)
    return nums[k-1]
    
print(largest([3,2,1,5,6,4],2))