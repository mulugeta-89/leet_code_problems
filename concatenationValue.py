def concatenationValue(arr):
    concatenationValue = 0
    conca = ""
    left = 0
    right = len(arr)-1
    mid = len(arr)//2
    if len(arr) % 2 == 0:
        while left < mid:
            conca = str(arr[left]) + str(arr[right-left])
            concatenationValue += int(conca)
            left += 1
    else:
        while left < mid:
            conca = str(arr[left]) + str(arr[right-left])
            concatenationValue += int(conca)
            left += 1
        concatenationValue += arr[mid]


    return concatenationValue
print(concatenationValue([5,14,13,8,12]))

