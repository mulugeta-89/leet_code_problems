def counting_element(arr):
    total = 0
    for i in range(len(arr)):
        for j in range(0, len(arr)):
            if arr[i]+1 == arr[j]:
                total += 1
                break
    return total
print(counting_element([1,1,2,2]))