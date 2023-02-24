def longestSubsequence(nums):
    counter = 1
    sol_arr = []
    for i in range(len(nums)-1):
        if nums[i] < nums[i+1]:
            counter += 1
            sol_arr.append(counter)
        else:
            counter = 1
    return max(sol_arr) if len(sol_arr) > 0 else counter
print(longestSubsequence([1,3,5,4,2,3,4,5]))