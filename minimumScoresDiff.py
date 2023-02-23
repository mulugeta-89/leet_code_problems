def minDifference(nums,k):
    ans = max(nums)
    right = k-1
    left = 0
    while right < len(nums):
        mini = nums[right]-nums[left]
        ans = min(ans, mini)
        left+= 1
        right += 1
    return ans
print(minDifference([90],1))


