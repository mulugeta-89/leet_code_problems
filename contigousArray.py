def conti(nums):
    count_dict = {}
    count = 0
    count_dict[0] = -1
    maxi = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            count -= 1
        if nums[i] == 1:
            count += 1
        if count in count_dict:
            maxi = max(maxi, i-count_dict[count])
        else:
            count_dict[count] = i
    return maxi
print(conti([0,1,0,0,0,0,1,0,1]))
