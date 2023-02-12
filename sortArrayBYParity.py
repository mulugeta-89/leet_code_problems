def sortArray(nums):
    newArray = sorted(nums, key=lambda x: x%2)
    return newArray
print(sortArray([1,2,3,4]))