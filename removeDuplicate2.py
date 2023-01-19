def removeDuplicate(arr):
    prev = arr[0]
    index = 1
    for i in range(1,len(arr)):
        if arr[i] != prev:
            arr[index] = arr[i]
            index = index + 1
            prev = arr[i]
    
    return index
print(removeDuplicate([0,0,1,1,1,2,2,3,3,4]))