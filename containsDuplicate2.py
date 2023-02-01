def containsDuplicate(nums,k):
    nums_dict = {}
    for i,n in enumerate(nums):
        if n not in nums_dict:
            nums_dict[n] = i
        else:
            dif = abs(i-nums_dict[n])
            if dif <= k:
                return True
            nums_dict[n] = i
    return False


print(containsDuplicate([1,2,3,1,2,3],2))