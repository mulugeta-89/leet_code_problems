def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
            if min_idx != i:
                temp = arr[i]
                arr[i] = arr[min_idx]
                arr[min_idx] = temp
arr = [6,7,5,7,8,5]
selection_sort(arr)
print(arr)
