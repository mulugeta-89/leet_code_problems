def nextGreaterNumber(nums1, nums2):
    ans = []
    for i in range(len(nums1)):
        counter = 0
        if nums1[i] in nums2:
            if nums2[nums2.index(nums1[i])] == nums2[len(nums2)-1]:
                ans.append(-1)
            else:
                for k in range(nums2.index(nums1[i])+1,len(nums2)):
                    if nums2[k] > nums1[i]:
                        counter += 1
                        ans.append(nums2[k])
                        break
                if counter == 0:
                    ans.append(-1)
    return ans
print(nextGreaterNumber([2,1,3],[2,3,1]))
    