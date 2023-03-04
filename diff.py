def diff(nums1, nums2):
    sol_arr1 = []
    sol_arr2 = []
    for item in nums1:
        if item not in nums2:
            sol_arr1.append(item)

    for item in nums2:
        if item not in nums1:
            sol_arr2.append(item)
    return [list(set(sol_arr1)), list(set(sol_arr2))]
print(diff([1,2,3],[2,4,6]))