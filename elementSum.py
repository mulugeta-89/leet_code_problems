def elementSum(arr):
    element_sum = sum(arr)
    digit_sum = 0
    for item in arr:
        item = str(item)
        if len(item) >=1:
            for little_item in item:
                digit_sum += int(little_item)
    return abs(element_sum - digit_sum)
print(elementSum([1,15,6,7]))

