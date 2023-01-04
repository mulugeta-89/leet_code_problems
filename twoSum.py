list1 = [3,2,3]
def twoSum(arr, target):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)+1):
            if arr[i]+arr[j] == target:
                return [i,j]

print(twoSum(list1, 5))