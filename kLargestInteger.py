def largest(nums,k):
    nums.sort(key=lambda x: int(x), reverse=True)
    return nums[k-1]
print(largest(["3","6","7","10"], 4))