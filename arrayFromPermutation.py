def arrayFromPermutation(arr):
    new_arr = []
    for i in range(len(arr)):
        first_item = arr[i]
        second_item = arr[first_item]
        new_arr.append(second_item)
    return new_arr
print(arrayFromPermutation([0,2,1,5,3,4]))