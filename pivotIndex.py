def pivotIndex(nums):
    sumLeft = 0
    sumRight = sum(nums)
    for i,x in enumerate(nums):
        if sumLeft == (sumRight-sumLeft-x):
            return i
        sumLeft += x
    return -1

print(pivotIndex([1,7,3,6,5,6]))

    