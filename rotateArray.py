def partition(nums, k):
    n = len(nums)
    if k > n:
        k = k%n
    first = nums[:n-k]
    second = nums[n-k:]
    sol = second + first
    nums[:] = sol[:]
    
print(partition([1,2,3,4,5,6,7], 15))


