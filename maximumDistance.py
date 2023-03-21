def maxi(nums1, nums2):
    maxi = 0
    i,j = 0,0
    while i < len(nums1) and j < len(nums2):
        if nums2[j] >= nums1[i]:
            maxi = max(maxi, j-i)
            j += 1
        else:
            i+=1
    return maxi

print(maxi([2,2,2], [10,10,7,7,6,5,4,3,2,1]))
